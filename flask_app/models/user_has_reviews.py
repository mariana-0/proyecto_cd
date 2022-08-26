from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class UserReview:
    def __init__(self,data):
        self.id=data['id']
        self.user_like_id=data['user_like_id']
        self.review_id=data['review_id']

    @classmethod
    def insert_like(cls,form):
        query='INSERT INTO users_has_reviews (user_like_id, review_id) VALUES (%(user_like_id)s,%(review_id)s)'
        result=connectToMySQL('proyecto').query_db(query,form)
        return result