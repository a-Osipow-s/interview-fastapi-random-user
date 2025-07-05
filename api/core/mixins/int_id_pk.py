from sqlalchemy.orm import Mapped, mapped_column


class IntIdPkMixin:
    """id primary key mixin"""
    id: Mapped[int] = mapped_column(primary_key=True)