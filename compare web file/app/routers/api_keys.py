from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session

from .. import models
from ..dependencies import get_db
from ..security import generate_api_key
from ..templating import templates

router = APIRouter(prefix="/keys", tags=["api-keys"])


@router.get("")
def list_keys_page(request: Request, db: Session = Depends(get_db)):
    keys = db.query(models.ApiKey).order_by(models.ApiKey.created_at.desc()).all()
    return templates.TemplateResponse(request, "keys.html", {"keys": keys})


@router.post("")
def create_key(request: Request, name: str = Form(...), db: Session = Depends(get_db)):
    raw_key, prefix, key_hash = generate_api_key()
    api_key = models.ApiKey(name=name, prefix=prefix, key_hash=key_hash)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    # Rendered fragment: an out-of-band banner showing the raw key once,
    # plus the new table row for the normal hx-target swap.
    return templates.TemplateResponse(
        request,
        "partials/key_created.html",
        {"key": api_key, "raw_key": raw_key},
    )


@router.post("/{key_id}/revoke")
def revoke_key(request: Request, key_id: int, db: Session = Depends(get_db)):
    api_key = db.query(models.ApiKey).filter(models.ApiKey.id == key_id).first()
    if api_key:
        api_key.revoked = True
        db.commit()
        db.refresh(api_key)
    return templates.TemplateResponse(request, "partials/key_row.html", {"key": api_key})
