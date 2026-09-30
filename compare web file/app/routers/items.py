from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_api_key, get_db

router = APIRouter(prefix="/api/items", tags=["items"])


@router.get("", response_model=list[schemas.ItemOut])
def list_items(db: Session = Depends(get_db), api_key: models.ApiKey = Depends(get_api_key)):
    return db.query(models.Item).all()


@router.post("", response_model=schemas.ItemOut)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    api_key: models.ApiKey = Depends(get_api_key),
):
    db_item = models.Item(name=item.name, created_by_key_id=api_key.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
