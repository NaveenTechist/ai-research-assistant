from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from .base import Base


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    doc_id = Column(String, unique=True, nullable=False)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    upload_timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    total_pages = Column(Integer, default=0)
    total_chunks = Column(Integer, default=0)

    processing_status = Column(
        String,
        default="PENDING"
    )

    category = Column(String, default="Unknown")