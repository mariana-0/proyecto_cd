from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_app.models.user_has_reviews import UserReview
from flask_app.models.review import Review
from datetime import datetime, timedelta, date

@app.route('/create_review/<int:id>')
def create_review(id):
    if not 'id' in session:
        return redirect('/login')
    data = {'id':id}
    data_user = {'id':session['id']}
    movie=Movie.view_by_id(data)
    user=User.user_by_id(data_user)
    return render_template('create_review.html', movie=movie, user=user)

@app.route('/insert_review', methods=['POST'])
def insert_review():
    if not Review.valid_review(request.form):
        return redirect('/create_review/'+request.form['movie_id'])
    Review.create_review(request.form)
    return redirect('/view_movies')

@app.route('/view_reviews/<int:id>')
def view_reviews_by_movie(id):
    if not 'id' in session:
        return redirect('/login')
    data={'movie_id':id}
    data_movie={'id':id}
    data_user = {'id':session['id']}
    movie=Movie.view_by_id(data_movie)
    reviews=Review.view_reviews_by_movie(data)
    user = User.user_by_id(data_user)
    return render_template('view_reviews_by_movie.html', reviews=reviews, movie=movie, user=user)

@app.route('/insert_like', methods=['POST'])
def insert_like():
    UserReview.insert_like(request.form)
    return redirect('/view_reviews/'+request.form['movie_id'])
