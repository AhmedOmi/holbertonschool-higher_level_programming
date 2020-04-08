#!/usr/bin/python3
""" All states via SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_states():
    """List states from database"""

    argument = sys.argv
    url_base = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db_url = url_base.format(argument[1], argument[2], argument[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).order_by(State.id):
        print(i.id, ": ", i.name, sep="")

if __name__ == "__main__":
    list_states()
