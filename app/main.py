from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.api import router
from app.db import models
from app.db.session import engine, Session

models.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router, prefix='/api')

    return application


app = get_application()
