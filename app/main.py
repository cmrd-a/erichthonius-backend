from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.api import router


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

#
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     request.state.db = Session()
#     response = await call_next(request)
#     request.state.db.close()
#     return response



