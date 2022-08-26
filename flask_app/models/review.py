from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Review:
    def __init__(self,data):
        self.id=data['id']
        self.content=data['content']
        self.rate=data['rate']
        self.movie_id=data['movie_id']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        self.nickname=data['nickname']
        
    @classmethod
    def create_review(cls,form):
        query='INSERT INTO reviews (content, rate, movie_id, user_id) VALUES (%(content)s, %(rate)s, %(movie_id)s, %(user_id)s)'
        result = connectToMySQL('proyecto').query_db(query,form)
        return result
    
    @classmethod
    def view_reviews_by_movie(cls,data):
        query='SELECT reviews.*, movies.*, users.nickname AS nickname FROM reviews LEFT JOIN movies ON movies.id=reviews.movie_id LEFT JOIN users ON reviews.user_id=users.id WHERE reviews.movie_id = %(movie_id)s;'
        results = connectToMySQL('proyecto').query_db(query, data)
        print(results)
        reviews=[]
        for review in results:
            ins_review=cls(review)
            reviews.append(ins_review)
        return reviews
    
    @staticmethod
    def valid_review(form):
        is_valid=True
        query = 'SELECT * FROM reviews WHERE user_id=%(user_id)s AND movie_id=%(movie_id)s'
        results = connectToMySQL('proyecto').query_db(query,form)
        if len(results)>=1:
            flash('You already reviewed this movie', 'create_review')
            is_valid=False
        if int(form['rate'])>5 or int(form['rate'])<1:
            flash('Enter a valid rate', 'create_review')
            is_valid=False
        if len(form['content'])<7:
            flash('Content at least 7 characters', 'create_review')
            is_valid=False
        return is_valid