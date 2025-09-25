import datetime

from sqlalchemy import String, Text, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column

from api.enums.books import BooksType
from api.models.base import Base
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin


class Book(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    title: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        nullable=False
    )

    short_description: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text, 
        nullable=True,
    )

    public_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    type: Mapped[BooksType] = mapped_column(
        Enum(BooksType),
        nullable=False,
        default=BooksType.FICTION
    )
