import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

# change this in production while deployment of the website to a string password
app.config['SECRET_KEY'] = 'mysecretkey'

####### DATABASE SETUP ###########
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


##############################
#########Login configs#########

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message_category = 'info'
login_manager.login_view = 'users.login'


from unbillit_project.core.views import core
from unbillit_project.user.views import users
from unbillit_project.errors_pages.handlers import error_pages
from unbillit_project.dashboard.views import dashboard_views



app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(dashboard_views)
