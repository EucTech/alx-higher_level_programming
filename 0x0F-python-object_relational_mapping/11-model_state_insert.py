#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    
    print(state.id)

    session.close()
