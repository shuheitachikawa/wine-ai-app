from sqlalchemy import Column, String, Integer, Float
from pydantic import BaseModel
from db import Base
from db import engine

class WineAttributeTable(Base):
  __tablename__='wine_attributes'
  id = Column(
    Integer,
    primary_key = True,
    autoincrement = True
  )
  japanese_title = Column(String(256))
  english_title = Column(String(256))
  max_value = Column(Float)
  min_value = Column(Float)
  step = Column(Float)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class WineAttribute(BaseModel):
    id: int
    japanese_title: str
    english_title: str
    max_value: float
    min_value: float
    step: float


def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=engine)
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    main()
