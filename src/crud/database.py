from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .settings import settings


engine = create_engine(
    settings.database_url
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)


Base = declarative_base()


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()