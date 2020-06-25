from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request
from flask_login import (login_user, login_required, current_user, logout_user)
from unbillit_project import db
from unbillit_project.models import User
from unbillit_project.user.forms import RegistrationForm, LoginForm, UpdateUserForm
from unbillit_project.user.pic_handler import add_profile_pic
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__)


# REGISTER
@users.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard.welcome'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered! Please login or click forget password to reset your password', 'success')
            return redirect(url_for('users.login'))

        db.session.add(user)
        db.session.commit()
        flash(
            f'Accound created for {form.first_name.data} {form.last_name.data}','success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


# LOGIN
@users.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard.welcome'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Login Success!..', 'success')

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.welcome'))

        else:
            flash('Login Unsuccessful. Please check your email and password', 'success')

    return render_template('login.html', form=form)


# LOGOUT
@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.home'))


# ACCOUNT INFO
@users.route('/account-info', methods=['GET', 'POST'])
@login_required
def account_info():

    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.profile_img.data:
            pic = add_profile_pic(form.profile_img.data)
            current_user.profile_img = pic

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data

        db.session.commit()
        flash('Your Account has been Updated!..', 'success')
        return redirect(url_for('users.account_info'))

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email

    profile_img = url_for(
        'static', filename='profile_pics/' + current_user.profile_img)

    return render_template('account.html', profile_img=profile_img, form=form)
