from flask import Blueprint,render_template,request
from flask_login import current_user
from webproject.models import Users
from webproject import db
from flask_login import login_required
from datetime import datetime as dt


main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/welcome')
@login_required
def welcome():
    return render_template('main/welcome.html',first_name=current_user.first_name,last_name=current_user.last_name)



