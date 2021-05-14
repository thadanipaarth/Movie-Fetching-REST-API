"""
Movies module
"""
from flask import (
    make_response,
    abort,
)
from config import db
from models import (
    Movies,
    MoviesSchema,
)
import connexion

def read_all(sortby=None,order='asc'):
	"""
		Purpose: Reading all the rows from the 'movies' table and sort them, if needed
		Parameters: - sortby (Default=None) (optional)
					- order (Default='asc') (optional)
	"""
	
	# Error handling for invalid specified order.
	if order != "asc" and order != "desc":
		abort(
			400,
			'Order must be ascending(asc) or descending(desc)'
		)
	
	if sortby is None: # If sorting parameter is not passed. 
		
		# Error handling, If the order is passed, the context of the order is not clear.
		if 'order' in connexion.request.args:
			abort(
				400,
				'Sorting parameter was not specified in the request'
			)
		else: # No sort and No Order passed
			movies_data= Movies.query.all()

	else:
		if sortby == "name":
			# Sorting with respect to Name
			if order == "asc": # Ascending order
				movies_data= Movies.query.order_by(Movies.name).all()
			else: # Descending Order
				movies_data= Movies.query.order_by(Movies.name.desc()).all()

		elif sortby == "year":
			# Sorting with respect to Year
			if order == "asc": # Ascending order
				movies_data= Movies.query.order_by(Movies.year).all()
			else: # Descending Order
				movies_data= Movies.query.order_by(Movies.year.desc()).all()

		elif sortby == "rating":
			# Sorting with respect to Rating
			if order == "asc": # Ascending order
				movies_data= Movies.query.order_by(Movies.rating).all()
			else: # Descending Order
				movies_data= Movies.query.order_by(Movies.rating.desc()).all()
		else: # Error Handling, Invalid sorting parameter
			abort(
				400,
				'Sorting parameter not found, please refer documentation for available parameters'
			)

	movies_schema=MoviesSchema(many=True)
	return movies_schema.dump(movies_data)

def searchbyname(value):
	"""
		Purpose: to search the movies with a particular name
		Parameters: - value (name of the movie)
	"""
	movies= Movies.query.filter(Movies.name == value).all()

	if len(movies) != 0:
		movies_schema=MoviesSchema(many=True)
		return movies_schema.dump(movies)

	else:
		abort(
			404,
			"Movie for the name: {name}, was not found".format(name=value)
		)

    

