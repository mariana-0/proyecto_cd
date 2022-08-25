from flask import render_template, request, redirect, session, flash
from flask_app import app
#from flask_app.models.user import User
from flask_app.models.movie import Movie
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