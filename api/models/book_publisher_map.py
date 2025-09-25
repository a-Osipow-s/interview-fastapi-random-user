from sqlalchemy import Column, ForeignKey, Table

from api.models.base import Base


book_publisher_map = Table(
    "book_publisher_map",
    Base.metadata,
    Column(
        "book_id",
        ForeignKey("book.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "publisher_id",
        ForeignKey("publisher.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
