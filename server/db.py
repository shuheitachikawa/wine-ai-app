from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session


# 接続したいDBの基本情報を設定
user_name = "root"
password = "tachikawa"
host = 'db' #"localhost"  # docker-composeで定義したMySQLのサービス名
database_name = "wine_ai"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

Base = declarative_base()

# Sessionの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class WineAttribute(Base):
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


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()



def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=engine)
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    main()
