# coding=utf-8

# 1 - imports
from datetime import date

from model import Actor, ContactDetails, Movie, Stuntman
from base import Session, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

session = Session()


# Create

bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
session.add(bourne_identity)
session.commit()

# Read

movie = session.query(Movie) \
    .filter(Movie.title == "The Bourne Identity") \
    .first()

if movie:
    print(f"the movie title is {movie.title}")

# Update

movie.title = "The Bourne Identity has changed"

print(f"the movie title is {movie.title}")

session.commit()


# Delete

session.delete(movie)

session.commit()

movie = session.query(Movie) \
    .filter(Movie.title == "The Bourne Identity") \
    .first()

if movie:
    print("the movie has not being deleted")
else:
    print("the you are loking for is deleted")


session.close()

