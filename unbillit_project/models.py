from flask_wtf import FlaskForm
from unbillit_project import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_img = db.Column(db.String(64), nullable=False,
                            default='default_profile.png')
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    password = db.Column(db.String(256))

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

        
class ContactUs(db.Model):

    __tablename__ = 'contact_us'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    message = db.Column(db.String(2048), nullable=False)

    def init(self, name, email, message):

        self.name = name
        self.email = email
        self.message = message
