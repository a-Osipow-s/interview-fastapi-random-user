from datetime import datetime
from typing import List

from sqlalchemy import Enum, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.attachments.models import Attachment
from api.comments.models import Comment
from api.core.base import Base
from api.core.mixins.int_id_pk import IntIdPkMixin
from api.core.mixins.dates import CreatedAtMixin, UpdateAtMixin

from api.users.constants import Language, Timezone, UserStatus


class UserCore(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(40), nullable=False)
    last_name: Mapped[str] = mapped_column(String(40), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), nullable=False)
    avatar_id: Mapped[int] = mapped_column(ForeignKey("attachment.id"), nullable=True)

    detail: Mapped["UserDetail"] = relationship(
        back_populates="user_core",
        uselist=False
    )
    avatar: Mapped["Attachment"] = relationship(
        back_populates="user_core",
        uselist=False
    )
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
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