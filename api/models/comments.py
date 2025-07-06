
from typing import List, TYPE_CHECKING

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin

if TYPE_CHECKING:
    from api.models import UserCore, TaskCore


class Comment(CreatedAtMixin, UpdateAtMixin, IntIdPkMixin, Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user_core.id"), nullable=False)
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task_core.id", ondelete="CASCADE"), 
        nullable=False
    )
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    parent_comment_id: Mapped[int] = mapped_column(
        ForeignKey("comment.id", ondelete="CASCADE"),
        nullable=True
    )

    parent: Mapped["Comment"] = relationship(
        remote_side="Comment.id",
        back_populates="replies"
    )
    replies: Mapped[List["Comment"]] = relationship(
        back_populates="parent",
        cascade="all, delete-orphan"
    )

    user: Mapped["UserCore"] = relationship(
        back_populates="comments",
    )
    task: Mapped['TaskCore'] = relationship(
        back_populates="comments"
    )