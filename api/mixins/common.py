from datetime import datetime 
from pydantic import BaseModel

class TimestampMixin(BaseModel):
    created_at: datetime = datetime.now()
    created_at: datetime = datetime.now()
