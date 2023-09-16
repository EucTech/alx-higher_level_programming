#!/usr/bin/python3
"""a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    stateName = sys.argv[4]

    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).\
        filter_by(name=stateName).all()

    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
