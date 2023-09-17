#!/usr/bin/python3
""" a script that lists all City objects from the database hbtn_0e_101_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(City.state_id == State.id).\
        order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")

    session.commit()
    session.close()
