#!/usr/bin/python3
""" a script that lists all State objects from the
database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

engine = create_engine(db_url, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
Session = Session()

result = Session.query(State).order_by(State.id).all()

for state in result:
    print("{}: {}".format(state.id, state.name))
