#!/usr/bin/python3
""" First state"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_first():
    """ list first state """
    argument = sys.argv
    base_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db = base_url.format(argument[1], argument[2], argument[3])
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).first()
    if i is not None:
        print(i.id, ": ", i.name, sep="")
    else:
        print(Nothing)


if __name__ == "__main__":
    list_first()
