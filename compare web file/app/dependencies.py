from datetime import datetime

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal
from .security import hash_key


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_api_key(
    x_api_key: str = Header(..., alias="X-API-Key"),
    db: Session = Depends(get_db),
) -> models.ApiKey:
    key_hash = hash_key(x_api_key)
    api_key = (
        db.query(models.ApiKey)
        .filter(models.ApiKey.key_hash == key_hash, models.ApiKey.revoked.is_(False))
        .first()
    )
    if api_key is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or revoked API key")

    api_key.last_used_at = datetime.utcnow()
    db.commit()
    return api_key
