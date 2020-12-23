from typing import ContextManager
from contextlib import contextmanager

from app.core.settings import settings
from sqlalchemy import Integer, Column, create_engine, Float
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import JSON

Base = declarative_base()


class Measurement(Base):
    __tablename__ = 'measurements_7'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    words = Column(JSON, nullable=False)
    said_words = Column(JSON, nullable=False)
    timings = Column(JSON, nullable=False)
    accuracy = Column(Float, nullable=False)
    wps = Column(Float, nullable=False)
    sps = Column(Float, nullable=False)


engine = create_engine(settings.PGSQL)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


@contextmanager
def session_scope() -> ContextManager[Session]:
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
