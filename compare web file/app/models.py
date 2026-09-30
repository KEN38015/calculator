from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from .database import Base


class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    prefix = Column(String, nullable=False)  # short, safe-to-display fragment
    key_hash = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_used_at = Column(DateTime, nullable=True)
    revoked = Column(Boolean, default=False)


class Item(Base):
    """Example resource protected by an API key."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_by_key_id = Column(Integer, ForeignKey("api_keys.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
