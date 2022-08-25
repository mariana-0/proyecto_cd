from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Movie:
    
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.year=data['year']
        self.genre=data['genre']
        self.director=data['director']
        self.country=data['country']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    @classmethod
    def insert_movie(cls, form):
        query='INSERT INTO movies (name, year, genre, director, country) VALUES (%(name)s,%(year)s,%(genre)s,%(director)s,%(country)s)'
        result=connectToMySQL('proyecto').query_db(query,form)
        return result
    
    @classmethod
    def view_movies(cls):
        query='SELECT * FROM movies'
        results=connectToMySQL('proyecto').query_db(query)
        movies=[]
        for movie in results:
            inst_movie=cls(movie)
            movies.append(inst_movie)
        return movies
    
    @classmethod
    def count_movies(cls):
        query = 'SELECT count(*) FROM movies'
        results = connectToMySQL('proyecto').query_db(query)
        return results[0]
    
    @classmethod
    def view_by_id(cls,data):
        query = 'SELECT * FROM movies WHERE id=%(id)s'
        result = connectToMySQL('proyecto').query_db(query,data)
        print('hiiiiiiiiii', result)
        movie = cls(result[0])
        return movie
    
    @classmethod
    def update_movie(cls,form):
        query = 'UPDATE movies SET name=%(name)s, year=%(year)s, director=%(director)s, country=%(country)s WHERE id=%(id)s'
        result=connectToMySQL('proyecto').query_db(query,form)
        return result
    
    @classmethod
    def update_genre(cls,form):
        query = 'UPDATE movies SET genre=%(genre)s WHERE id=%(id)s'
        result=connectToMySQL('proyecto').query_db(query,form)
        return result
    
    @classmethod
    def delete_movie(cls,data):
        query='DELETE FROM movies WHERE id=%(id)s'
        result=connectToMySQL('proyecyo').query_db(query,data)
        return result
    
    @staticmethod
    def valid_movie(form):
        is_valid=True
        if form['name']=='':
            flash('Missing name', 'create_movie')
            is_valid=False
        if len(form['year'])<4:
            flash('Enter a valid year', 'create_movie')
            is_valid=False
        if len(form['director'])<2:
            flash('Director at least two characteres', 'create_movie')
            is_valid=False
        if len(form['country'])<2:
            flash('Country at least two characteres','create_movie')
            is_valid=False
        return is_valid  