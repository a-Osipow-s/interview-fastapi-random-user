from datetime import datetime
from sqlalchemy.orm import DateTime, Mapped, mapped_column


class CreatedAtMixin:
    """created_at mixin"""
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class UpdateAtMixin:
    """updated_at mixin"""
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
