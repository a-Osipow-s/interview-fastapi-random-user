from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class TaskAttachmentMap(Base):
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        primary_key=True
    )
    attachment_id: Mapped[int] = mapped_column(
        ForeignKey("attachment.id", ondelete="CASCADE"), 
        primary_key=True
    )