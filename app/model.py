from sqlalchemy import Column, Integer, String

from .database import Base


class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(Integer, unique=True, index=True)
    domain = Column(String, unique=True, index=True)
