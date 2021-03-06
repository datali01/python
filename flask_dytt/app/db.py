from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .import db

BaseModel = declarative_base()

class Film(db.Model):
    __tablename__ = 'film'
    uid = Column(Integer, primary_key=True)
    name_cn = Column(String(100))
    name = Column(String(50))
    year = Column(String(10))
    country = Column(String(30))
    category = Column(String(30))
    language = Column(String(20))
    subtitle = Column(String(20))
    release_date = Column(String(50))
    score = Column(String(30))
    file_size = Column(String(10))
    movie_duration = Column(String(20))
    director = Column(String(30))
    image_name = Column(String(50))
    download_url = Column(String(500))
