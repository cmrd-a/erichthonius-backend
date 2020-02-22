from fastapi import APIRouter

from app.routes import base, files, periods


router = APIRouter()
router.include_router(base.router)
router.include_router(files.router, prefix="/files")
router.include_router(periods.router, prefix="/periods")
