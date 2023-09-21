from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str


class ShowUser(BaseModel):
    id: int
    username: str
    email: str
    blogs: List[Blog]


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    scopes: list[str] = []
