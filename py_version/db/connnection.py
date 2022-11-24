from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def init_db():
    engine = create_engine("sqlite:///local_file.db", echo=True, future=True)
    return scoped_session(sessionmaker(bind=engine))


engine = create_engine("sqlite:///local_file.db", echo=False)
db_session = scoped_session(sessionmaker(bind=engine))
# db_session = init_db()
