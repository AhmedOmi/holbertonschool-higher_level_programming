#!/usr/bin/python3
""" class inherite"""

from sqlalchemy import (
    inspect,
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class state"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False
                )
    name = Column(String(128), nullable=False)
