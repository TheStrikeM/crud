from enum import Enum
from typing import Optional
from datetime import date

from pydantic import BaseModel


class Lgbt(str, Enum):
    GEY = "GEY"
    NATURAL = "NATURAL"


class UserBase(BaseModel):
    name: str
    age: int
    desc: Optional[str]
    lgbt: Lgbt
    date: date


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
