from flask import Blueprint,render_template,request
from flask_login import current_user
from webproject.models import Users
from webproject import db
from flask_login import login_required
import json

mol = Blueprint('mol',__name__)

@mol.route('/molecules')
@login_required
def index():
    mols = json.load(open('./molecules.json','r'))
    return render_template('molecules/index.html',mols=mols)
