from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from Docs.Doc import sub_app

app = FastAPI(docs_url=None, redoc_url=None, title="Web ACS", openapi_url="/api/openapi.json")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(ProductsRouter, tags=['products'])
# app.include_router(UserRouter, tags=['users'])
# app.include_router(OrdersRouter, tags=['orders'])

app.mount("/api/docs", sub_app)
