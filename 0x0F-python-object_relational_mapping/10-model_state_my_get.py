#!/usr/bin/python3
""" Get a state """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_states():
    """ list all state containe a """
    argument = sys.argv
    base_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db = base_url.format(argument[1], argument[2], argument[3])
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(State).filter(State.name == argument[4]).first()
    if x is not None:
        print(x.id)
    else:
        print("Not found")
if __name__ == "__main__":
    get_states()
