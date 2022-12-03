from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form['role']
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(savedEmail=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password) or (user.urole != role):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)        
    if role == "student":
        return redirect(url_for('main.profile'))
    else:
        return redirect(url_for('main.about'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    userEmail = request.form.get('email')
    print(userEmail)
    name = request.form.get('teamName')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    role = request.form['role']
    inventoryVal = {}
    teams = {}
    requestsReceived = {}
    teammates = {}
    if role:
        print(role)
        print(type(role))
    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(savedEmail=userEmail).first()
    for person in User.query.all():
        print(person.name)
        print(person.password)
        print(person.savedEmail)
        print(person.urole)
        print(person.teams)

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    if (password == confirmPassword):
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(
                        email=userEmail, 
                        savedEmail =userEmail,
                        name=name,
                        password=generate_password_hash(
                            password, method='sha256'),
                        urole=role, 
                        inventory=inventoryVal, 
                        teams=teams, 
                        received_requests=requestsReceived,
                        team_mates=teammates
                        )

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        if role == "student":
            return redirect(url_for('main.profile'))
        else:
            return redirect(url_for('main.about'))
    flash("Passwords don't match!")
    return redirect(url_for('auth.signup'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
