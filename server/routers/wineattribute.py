from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.requests import Request
from pydantic import BaseModel
from db import WineAttribute, engine, get_db

router = APIRouter()


# リクエストボディの定義
class WineAttributeCreate(BaseModel):
  japanese_title: str
  english_title: str
  max_value: float
  min_value:float
  step:float


@router.get("/")
def readWineAttributes(db: Session = Depends(get_db)):
    wineAttribute = db.query(WineAttribute).all()
    return wineAttribute


@router.get("/{wine_id}")
def readWineAttribute(wine_id: int, db: Session = Depends(get_db)):
    wine = db.query(WineAttribute).filter(WineAttribute.id == wine_id).first()
    return wine


@router.post("/")
def CreateWineAttribute(wine: WineAttributeCreate,  db: Session = Depends(get_db)):
    db_wine = WineAttribute(
      japanese_title = wine.japanese_title,
      english_title = wine.english_title,
      max_value = wine.max_value,
      min_value = wine.min_value,
      step = wine.step
    )
    db.add(db_wine)
    db.commit()