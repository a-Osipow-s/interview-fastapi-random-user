
from typing import List, TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base
from api.models.task_attachment_map import task_attachment_map
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin

from api.constants.attachments import AttachmentUploadStatus

if TYPE_CHECKING:
    from api.models import TaskCore, UserCore


class Attachment(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    link: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    upload_status: Mapped[AttachmentUploadStatus] = mapped_column(
        Enum(AttachmentUploadStatus), nullable=False
    )

    user_core: Mapped["UserCore"] = relationship(back_populates="avatar")
    tasks: Mapped[List["TaskCore"]] = relationship(
        back_populates="attachments",
        secondary=task_attachment_map,
        cascade="all, delete"
    )