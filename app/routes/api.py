from fastapi import APIRouter

from app.routes import base
from app.routes import files

router = APIRouter()
router.include_router(base.router)
router.include_router(files.router, prefix="/files")
