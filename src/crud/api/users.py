from typing import Optional

from fastapi import APIRouter, Depends

from ..models.users import Lgbt
from ..services.users import UserService


router = APIRouter(
    prefix="/users"
)


@router.get("/")
async def get_all(
    lgbt: Optional[Lgbt] = None,
    service: UserService = Depends()
):
    return service.get_all(lgbt)


@router.get("/{user_id}")
async def get_user(
    user_id: int,
    service: UserService = Depends()
):
    return service.get(user_id)