from typing import List

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.users.models import UserCore
from api.tasks.models import TaskCore, TaskAttachmentMap
from api.core.base import Base
from api.core.mixins.int_id_pk import IntIdPkMixin
from api.core.mixins.dates import CreatedAtMixin, UpdateAtMixin

from api.attachments.constants import AttachmentUploadStatus


class Attachment(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    link: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    upload_status: Mapped[AttachmentUploadStatus] = mapped_column(
        Enum(AttachmentUploadStatus), nullable=False
    )

    user_core: Mapped["UserCore"] = relationship(back_populates="avatar")
    tasks: Mapped[List["TaskCore"]] = relationship(
        back_populates="attachments",
        secondary=TaskAttachmentMap,
        cascade="all, delete"
    )