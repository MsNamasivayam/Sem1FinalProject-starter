"""
The file that holds the logic to
initialize and connect to the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# Creates the engine to connect with our database.
# Set echo=True to see every SQL statement SQLAlchemy runs.
engine = create_engine("sqlite:///twitter.db", echo=False)

# The session we use to talk to the database
session = Session(engine)


# Base is the class all of our models will extend
class Base(DeclarativeBase):
    pass


def init_db():
    """
    Creates all of the tables. models must be imported first
    so that every class is registered on Base.metadata.
    """
    import models
    Base.metadata.create_all(engine)
