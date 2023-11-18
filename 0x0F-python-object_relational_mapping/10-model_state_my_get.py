#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_name_to_search = sys.argv[4]
    res = session.query(State).filter_by(name=state_name_to_search).first()
    if res:
        print(res.id)
    else:
        print("Not found")
    session.close()
