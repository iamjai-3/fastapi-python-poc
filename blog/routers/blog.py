from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, oauth2, schemas
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["Blogs"])
get_db = database.get_db


@router.get(
    "/",
    response_model=List[schemas.ShowBlog],
    status_code=status.HTTP_200_OK,
    tags=["Blogs"],
)
def getAll(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.create(request, db)


@router.get(
    "/{id}",
    response_model=schemas.ShowBlog,
    status_code=status.HTTP_200_OK,
    tags=["Blogs"],
)
def getOne(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_one(id, db)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.delete(id, db)
