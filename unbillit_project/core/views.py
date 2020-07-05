from flask import Blueprint, render_template

core = Blueprint('core', __name__)


@core.route('/')
def home():
    return render_template('home.html')


@core.route('/about')
def about():
    return render_template('about.html')

  
@core.route('/services')
def services():
    return render_template('services.html')


@core.route('/project')
def project():
    return render_template('project.html')
