from flask import render_template, request, redirect, session, flash
from flask_app import app
#from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_app.models.review import Review
from flask_bcrypt import Bcrypt   
from datetime import datetime, timedelta, date

@app.route('/create_movie')
def create_movie():
    if not 'id' in session:
        return redirect('/login')
    
    return render_template('create_movie.html')

@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    if not Movie.valid_movie(request.form):
        return redirect('/create_movie')
    Movie.insert_movie(request.form)
    return redirect('/home')

@app.route('/view_movie/<int:id>')
def view_movie(id):
    if not 'id' in session:
        return redirect('/login')
    data = {'id':id}
    movie=Movie.view_by_id(data)
    return render_template('view_movie.html', movie=movie)

@app.route('/edit_movie/<int:id>')
def edit_movie(id):
    if not 'id' in session:
        return redirect('/login')
    data = {'id':id}
    movie=Movie.view_by_id(data)
    return render_template('edit_movie.html',movie=movie)

@app.route('/update_movie', methods=['POST'])
def update_movie():
    if not Movie.valid_movie(request.form):
        return redirect('/edit_movie/'+request.form['id'])
    Movie.update_movie(request.form)
    return redirect('/view_movie/'+request.form['id'])

@app.route('/change_genre', methods=['POST'])
def change_genre():
    Movie.update_genre(request.form)
    return redirect('/view_movie/'+request.form['id'])

@app.route('/delete_movie/<int:id>')
def delete_movie(id):
    if not 'id' in session:
        return redirect('/login')
    data = {'id':id}
    Movie.delete_movie(data)
    return redirect('/home')

@app.route('/view_movies')
def view_all_movies():
    if not 'id' in session:
        return redirect('/login')
    movies=Movie.view_movies()
    return render_template('/view_movies.html',movies=movies)

@app.route('/search/<searchtype>', methods=['POST'])
def search_movies(searchtype):
    if searchtype=='genre':
        search_form='genre'
        movies=Movie.search_genre(request.form)
    elif searchtype=='country':
        search_form='country'
        movies=Movie.search_country(request.form)
    else:
        if not Movie.valid_years(request.form):
            return redirect('/home')
        search_form='year'
        movies=Movie.search_year(request.form)
    return render_template('search.html', search_form=search_form, movies=movies)