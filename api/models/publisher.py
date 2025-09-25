from sqlalchemy import String, Text, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.enums.publisher import PublisherStatus
from api.models.base import Base
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin


class Publisher(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    info: Mapped[str] = mapped_column(
        Text, nullable=False,
    )

    status: Mapped[PublisherStatus] = mapped_column(
        Enum(PublisherStatus),
        default=PublisherStatus.DRAFT,
        nullable=False,
    )

    status_history: Mapped[list['PublisherStatusHistory']] = relationship(
        back_populates='publisher',
        cascade="all, delete-orphan"
    )


class PublisherStatusHistory(IntIdPkMixin, CreatedAtMixin, Base):
    publisher_id: Mapped[int] = mapped_column(
        ForeignKey("publisher.id", ondelete="CASCADE"),
        nullable=False
    )

    previous_status: Mapped[PublisherStatus] = mapped_column(
        Enum(PublisherStatus),
        nullable=False,
    )

    current_status: Mapped[PublisherStatus] = mapped_column(
        Enum(PublisherStatus),
        nullable=False,
    )
    
    publisher: Mapped['Publisher'] = relationship(back_populates='status_history')
