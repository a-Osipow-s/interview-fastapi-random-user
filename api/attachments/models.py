from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.core.base import Base
from api.core.mixins.int_id_pk import IntIdPkMixin
from api.core.mixins.dates import CreatedAtMixin, UpdateAtMixin


class Attachment(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    link: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    upload_status: Mapped[str]
