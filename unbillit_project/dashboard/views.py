from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request
from flask_login import (login_user, login_required, current_user, logout_user)
from unbillit_project import db
from unbillit_project.models import User
from unbillit_project.user.forms import RegistrationForm, LoginForm, UpdateUserForm
from unbillit_project.user.pic_handler import add_profile_pic
from werkzeug.security import generate_password_hash, check_password_hash

dashboard_views = Blueprint('dashboard', __name__)


@dashboard_views.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')
