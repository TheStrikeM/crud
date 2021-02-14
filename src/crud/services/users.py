from typing import Optional, List

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.users import Lgbt, UserUpdate, UserCreate
from ..tables import users as tables


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int):
        user = (
            self.session
            .query(tables.Users)
            .filter_by(id=user_id)
            .first()
        )
        return user

    def get_all(self, lgbt: Optional[Lgbt] = None) -> List[tables.Users]:
        query = self.session.query(tables.Users)
        if lgbt:
            query.filter_by(lgbt=lgbt)
        return query.all()

    def get(self, user_id: int):
        return self._get(user_id)

    def create(self, user_data: UserCreate):
        user = tables.Users(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserUpdate):
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, user_id: int):
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()

