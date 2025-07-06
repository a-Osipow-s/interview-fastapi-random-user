from sqlalchemy import Column, ForeignKey, Table

from api.models.base import Base


task_attachment_map = Table(
    "task_attachment_map",
    Base.metadata,
    Column(
        "task_id", 
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        primary_key=True
    ),
    Column(
        "attachment_id", 
        ForeignKey("attachment.id", ondelete="CASCADE"), 
        primary_key=True
    )
)