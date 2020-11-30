from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import wineattribute, prediction

app = FastAPI()

origins = [
    # "http://localhost:3000",
    "*"
]

#CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ルーター定義
app.include_router(
    wineattribute.router,
    prefix="/api/wine-attributes",
    tags=["Wine Attribute"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    prediction.router,
    prefix="/api/prediction",
    tags=["Prediction"],
    responses={404: {"description": "Not found"}},
)

