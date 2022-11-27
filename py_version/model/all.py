from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, relationship
from db.connnection import db_session

Base = declarative_base()


class FileFinger(Base):
    __tablename__ = "file_finger"
    file_path = Column(String, primary_key=True)
    # driver_name = Column(String)
    finger = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


def sync_table():
    from db.connnection import engine
    Base.metadata.create_all(engine)


class _FileFingerManger(object):
    def __init__(self, db_session):
        self._db_session = db_session

    def get_by_file_path(self, f_path: str):
        return self._db_session.query(FileFinger).filter_by(file_path=f_path).first()

    def filter_start_with_file_path(self, f_path: str):
        return self._db_session.query(FileFinger).filter(FileFinger.file_path.like(f"{f_path}%")).all()


FileFingerM = _FileFingerManger(db_session)