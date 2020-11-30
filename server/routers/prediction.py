from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.requests import Request
from pydantic import BaseModel
from db import WineAttribute, engine, get_db
from services import PredictionService
from typing import List  # ネストされたBodyを定義するために必要


router = APIRouter()

# リクエストbodyを定義
class Input(BaseModel):
    id: int
    value: float


@router.post("/")
def Predict(inputs: List[Input]):
    attrs = []
    for input in inputs:
      attrs.append({"id": input.id, "value": input.value})
    res = PredictionService.predict(attrs)
    return res
