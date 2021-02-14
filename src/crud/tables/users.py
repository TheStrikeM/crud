import sqlalchemy as sa

from ..database import Base


class Users(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, default="User")
    desc = sa.Column(sa.String)
    age = sa.Column(sa.String, defualt="15")
    lgbt = sa.Column(sa.String)
    date = sa.Column(sa.Date)