from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_bcrypt import Bcrypt   
from datetime import datetime, timedelta, date

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/register')
def index_reg():
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register():
    if not User.validation(request.form):
        return redirect('/register')
    
    pwd = bcrypt.generate_password_hash(request.form['password'])
    
    form = {
        'nickname':request.form['nickname'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':pwd,
    }
    
    id=User.create_user(form)
    session['id']=id
    
    return redirect('/home')

@app.route('/login_user', methods=['POST'])
def login():
    user = User.user_by_email(request.form)
    if not user: 
        flash('Wrong email or deleted account', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password', 'login')
        return redirect('/')
    session['id']=user.id
    return redirect('/home')

@app.route('/home')
def home_reviews():
    if not 'id' in session:
        return redirect('/login')
    data = {
        'id': session['id']
    }
    user = User.user_by_id(data)
    users = User.get_all()
    count = User.count_users()
    movies=Movie.view_movies()
    count_m = Movie.count_movies()
    return render_template('home.html', user=user, users=users, count=count, movies=movies, count_m=count_m)

@app.route('/view_user')
def view_user():
    if not 'id' in session:
        return redirect('/login')
    data = {
        'id': session['id']
    }
    user = User.user_by_id(data)
    return render_template('view_user.html', user=user)

@app.route('/edit_user')
def edit_user():
    if not 'id' in session:
        return redirect('/login')
    data = {
        'id': session['id']
    }
    user = User.user_by_id(data)
    return render_template('edit_user.html', user=user)

@app.route('/update_user', methods=['POST'])
def update_user():
    if not User.valid_edit(request.form):
            return redirect('/edit_user')
    User.edit_user(request.form)
    return redirect('/view_user')

@app.route('/delete/<int:id>')
def delete_user(id):
    if not 'id' in session:
        return redirect('/login')
    data = {'id':id}
    User.delete_user(data)
    return redirect('/home')

@app.route('/change_password', methods=['POST'])
def change_password():
    if not 'id' in session:
        return redirect('/login')
    data = {
        'id': session['id']
    }
    user = User.user_by_id(data)
    if not bcrypt.check_password_hash(user.password, request.form['old_password']):
        flash('Wrong current password', 'password')
        return redirect('/edit_user')
    if not User.valid_password(request.form):
        return redirect('/edit_user')
    pwd1 = bcrypt.generate_password_hash(request.form['password'])
    form = {
        'id':request.form['id'],
        'password':pwd1
    }
    User.change_password(form)
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
