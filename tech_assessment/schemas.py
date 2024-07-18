from typing import Union
from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: Union[str, None] = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    __pydantic_config__ = ConfigDict(strict=True)
    id: int
    owner_id: int


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    __pydantic_config__ = ConfigDict(strict=True)
    id: int
    is_active: bool
    tasks: list[Task] = []


class LabelBase(BaseModel):
    label: str


class LabelCreate(LabelBase):
    pass


class Label(LabelBase):
    __pydantic_config__ = ConfigDict(strict=True)
