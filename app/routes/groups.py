from fastapi import APIRouter
from app.crud import crud
from fastapi import Depends, HTTPException
from app.schemas import schemas
from app.db.session import Session

from typing import List

router = APIRouter()


# Dependency
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = crud.get_group_by_name(db, name=group.name)
    if db_group:
        raise HTTPException(status_code=400, detail="Group already registered")
    return crud.create_group(db=db, group=group)


@router.get("/", response_model=List[schemas.Group])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups
