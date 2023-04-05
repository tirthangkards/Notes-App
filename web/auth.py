from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method=='POST':

        first_name=request.form.get('firstName')
        last_name=request.form.get('lastName')
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm_password=request.form.get('confirmPassword')

        user=User.query.filter_by(email=email).first()
        
        if user:
            flash("Email already exists", category='error')
        elif len(first_name)==0:
            flash('Enter First Name', category='error')
        elif len(last_name)==0:
            flash('Enter Last Name', category='error')
        elif len(username)==0:
            flash('Enter Username', category='error')
        elif len(email) < 5:
            flash('Enter a valid email', category='error')
        elif len(password) < 7:
            flash('Password must contain atleast 6 characters', category='error')
        elif password!=confirm_password:
            flash('Password mismatched', category='error')
        else:
            new_user=User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, confirm_password=confirm_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category='success')
            login_user(new_user, remember=True)
            session['user']=new_user.id
            return redirect(url_for('views.home'))

    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        
        user=User.query.filter_by(email=email).first()

        if user:
            if user.username == username:
                if user.password==password:
                    flash('Logged in', category='success')
                    login_user(user, remember=True)
                    session['user']=user.id
                    return redirect(url_for('views.home', user_name=username))
                else:
                    flash('Incorrect Password', category='error')
            else:
                flash('Incorrect Username')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html')

@auth.route('/logout', methods=['GET', 'POST'])
@login_required

def logout():
    if 'user' in session:
        session.pop('user')
    logout_user()
    return redirect(url_for('views.home'))