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
    a = "a"
    if a in x:
        print(x.id, ": ", x.name, sep="")
    else:
        print(Nothing)


if __name__ == "__main__":
    contain_a()
