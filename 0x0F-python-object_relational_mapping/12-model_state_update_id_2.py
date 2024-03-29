#!/usr/bin/python3

"""This module lists all states starting
from the database hbtn_0e_0_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """Create a configered'Session' class"""
    Session = sessionmaker(bind=engine)
    """Create a Session"""
    session = Session()
    """Query all State objects and sort by states.id"""
    changed_state = session.query(State).filter(State.id == 2).first()
    """Print the results"""
    if changed_state:
        changed_state.name = 'New Mexico'
        session.commit()
    else:
        print("Object with ID {} not found.".format(changed_state))
    """Close the session"""
    session.close()
