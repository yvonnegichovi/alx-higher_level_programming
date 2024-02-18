#!/usr/bin/python3

"""This module lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    """Create a configered'Session' class"""
    Session = sessionmaker(bind=engine)
    """Create a Session"""
    session = Session()
    """Query all Cities objects and sort by cities.id"""
    cities = session.query(State, City).filter(State.id == City.state_id)\
                        .order_by(City.id).all()
    """Prints the results"""
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    """Close the session"""
    session.close()
