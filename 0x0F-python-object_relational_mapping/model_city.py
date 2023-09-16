#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py
that contains the class definition of a City"""


from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """This is City class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("States.id"), nullable=False)
