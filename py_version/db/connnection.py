import logging
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

logger = logging.getLogger(__name__)

engine = create_engine("sqlite:///local_file.db", echo=False)
db_session = scoped_session(sessionmaker(bind=engine))


def scoped_db_session():
    def decorator(func):
        @wraps(func)
        def _fn(*args, **kwargs):
            session = db_session
            try:
                session()
                logger.debug('start db session')
                return func(*args, **kwargs)
            finally:
                session.remove()
                logger.debug('db session removed')

        return _fn

    return decorator
