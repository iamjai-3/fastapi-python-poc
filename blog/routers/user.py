from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import user

router = APIRouter(prefix="/user", tags=["Users"])
get_db = database.get_db


@router.post(
    "/",
    response_model=schemas.ShowUser,
    status_code=status.HTTP_201_CREATED,
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.ShowUser],
    status_code=status.HTTP_200_OK,
)
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)
