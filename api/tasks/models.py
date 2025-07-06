from typing import List

from sqlalchemy import String, Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.comments.models import Comment
from api.attachments.models import Attachment
from api.core.base import Base
from api.core.mixins.int_id_pk import IntIdPkMixin
from api.core.mixins.dates import CreatedAtMixin, UpdateAtMixin

from api.tasks.constants import TaskPriority, TaskStatus, TaskType


class TaskCore(CreatedAtMixin, UpdateAtMixin, IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    type: Mapped[TaskType] = mapped_column(Enum(TaskType), nullable=False)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), nullable=False)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), nullable=False)
    assigned_user_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id", ondelete="CASCADE"), 
        nullable=True
    )
    parent_task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        nullable=True
    )

    parent: Mapped["TaskCore"] = relationship(
        remote_side=[lambda: TaskCore.id],
        back_populates="subtasks"
    )
    subtasks: Mapped[List["TaskCore"]] = relationship(
        back_populates="parent",
        cascade="all, delete-orphan"
    )

    detail: Mapped["TaskDetail"] = relationship(
        back_populates="core_info",
        uselist=False,
        cascade="all, delete-orphan"
    )

    status_history: Mapped[List["TaskStatusHistory"]] = relationship(
        back_populates="task",
        cascade="all, delete-orphan"
    )

    assignees_history: Mapped[List["TaskAssigneesHistory"]] = relationship(
        back_populates="task",
        cascade="all, delete-orphan"
    )

    attachments: Mapped[List["Attachment"]] = relationship(
        back_populates="tasks",
        secondary="TaskAttachmentMap",
        cascade="all, delete"
    )
    
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="task",
        cascade="all, delete-orphan"
    )


class TaskDetail(Base):
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        primary_key=True
    )
    description: Mapped[str] = mapped_column(Text, nullable=True)
    resources: Mapped[str] = mapped_column(Text, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    core_info: Mapped["TaskCore"] = relationship(back_populates="detail")


class TaskAttachmentMap(Base):
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        primary_key=True
    )
    attachment_id: Mapped[int] = mapped_column(
        ForeignKey("attachment.id", ondelete="CASCADE"), 
        primary_key=True
    )


class TaskStatusHistory(CreatedAtMixin, IntIdPkMixin, Base):
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"),
        nullable=False,
    )
    previous_status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), nullable=True)
    current_status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), nullable=False)
    changed_by_user_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id"), 
        nullable=False,
    )

    task: Mapped["TaskCore"] = relationship(back_populates="status_history")


class TaskAssigneesHistory(CreatedAtMixin, IntIdPkMixin, Base):
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"),
        nullable=False,
    )
    previous_assignee_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id"), 
        nullable=True,
    )
    current_assignee_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id"), 
        nullable=False,
    )
    changed_by_user_id: Mapped[int] = mapped_column(
        ForeignKey("user_core.id"), 
        nullable=False,
    )

    task: Mapped["TaskCore"] = relationship(back_populates="status_history")