#!/usr/bin/python3
""" relationship City"""


from sqlalchemy import Integer, String, Column, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """This is City class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
