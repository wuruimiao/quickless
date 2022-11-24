from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, relationship

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