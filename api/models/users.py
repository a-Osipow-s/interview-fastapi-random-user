import bcrypt
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import Enum, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin

from api.constants.users import Language, Timezone, UserStatus

from api.utils.password import hash_password

if TYPE_CHECKING:
    from api.models import Attachment, Comment


class UserCore(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    email: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(40), 
        unique=True, 
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(String(40), nullable=False)
    last_name: Mapped[str] = mapped_column(String(40), nullable=False)
    _password: Mapped[str] = mapped_column(
        "password", 
        String(255), 
        nullable=False
    )
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus), 
        nullable=False, 
        default=UserStatus.CREATED
    )
    avatar_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("attachment.id"), 
        nullable=True
    )

    detail: Mapped[Optional["UserDetail"]] = relationship(
        back_populates="user_core",
        uselist=False
    )
    avatar: Mapped[Optional["Attachment"]] = relationship(
        back_populates="user_core",
        uselist=False
    )
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    @property
    def password(self):
        raise AttributeError("")

    @password.setter
    def password(self, password: str):
        self._password = hash_password(password).decode()

    def validate_password(self, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(
            password=self._password.encode(),
            hashed_password=hashed_password
        )   



class UserDetail(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id", ondelete="CASCADE"), 
        primary_key=True
    )
    bio: Mapped[str] = mapped_column(Text, deferred=True, nullable=True)
    job_title: Mapped[str] = mapped_column(String(50), nullable=True)
    language: Mapped[Language] = mapped_column(
        Enum(Language), 
        nullable=False, 
        default=Language.ENGLISH
    )
    timezone: Mapped[Timezone] = mapped_column(
        Enum(Timezone),
        nullable=False,
        default=Timezone.EUROPE_LONDON
    )
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    user_core: Mapped["UserCore"] = relationship(back_populates="detail")
