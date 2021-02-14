from typing import Optional

from fastapi import APIRouter, Depends, Response, status

from ..models.users import Lgbt, UserCreate, User
from ..services.users import UserService


router = APIRouter(
    prefix="/users"
)


@router.get("/", response_model=User)
async def get_all(
    lgbt: Optional[Lgbt] = None,
    service: UserService = Depends()
):
    return service.get_all(lgbt)


@router.post("/", response_model=User)
async def create_user(
    user_data: UserCreate,
    service: UserService = Depends()
):
    return service.create(user_data)


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    service: UserService = Depends()
):
    return service.get(user_id)


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    service: UserService = Depends()
):
    return service.update(user_id)


@router.delete("/{user_id}", response_model=User)
async def delete_user(
    user_id: int,
    service: UserService = Depends()
):
    service.delete(user_id)
    return Response(status_code=status.HTTP_404_NOT_FOUND)