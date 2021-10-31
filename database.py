from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_movie( pic_link, director, movie_name, release_year, price, description):
	movie_object=Movie(
	pic_link=pic_link,
	movie_name=movie_name,
	director=director,
  release_year=release_year,
	price=price,
	description=description)
	session.add(movie_object)
	session.commit()

def delete_movie(id):
	session.query(Movie).filter_by(id=id).delete()
	session.commit()

def query_all():

   movies = session.query(
      Movie).all()
   print(movies)
   return movies
