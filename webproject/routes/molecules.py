from flask import Blueprint,render_template,request
from flask_login import current_user
from webproject.models import Users
from webproject import db
from flask_login import login_required
import json

mol = Blueprint('mol',__name__)
mols = json.load(open('./molecules.json','r'))

@mol.route('/molecules')
@login_required
def index():
    return render_template('molecules/index.html',mols=mols)

@mol.route('/molecules/<zinc_id>')
@login_required
def molecule_detail(zinc_id):
    mol = mols[zinc_id]
    return render_template('molecules/molecule_detail.html',mol=mol,molecule=zinc_id)