#!/usr/bin/python3

"""
contains the class definition of a City and an instance
Base = declarative_base()
"""

import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """
    Inherits from Base
    links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
