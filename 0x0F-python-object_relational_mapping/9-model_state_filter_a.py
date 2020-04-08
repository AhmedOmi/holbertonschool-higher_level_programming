#!/usr/bin/python3
""" Contains `a` """

import sys
from model_state import Base, State
from sqlalchemy import create_engine


def contain_a():
    """ list all state containe a """
    argument = sys.argv
    base_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db = base_url.format(argument[1], argument[2], argument[3])
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(State)
     for i in x.filter(State.name.like('%a%')):
        print(inst.id, ": ", inst.name, sep="")
if __name__ == "__main__":
    contain_a()
