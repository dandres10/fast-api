from bd.database import Base
from sqlalchemy import Column, Integer, String, Float, Sequence


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, Sequence('usuario_id_seq'),primary_key=True)
    title = Column(String(50))
    overview = Column(String(50))
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String(50))
