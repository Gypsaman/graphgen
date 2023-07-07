from flask import Blueprint,render_template,request
from flask_login import current_user
from webproject.models import Users
from webproject import db
from flask_login import login_required
import json

mol = Blueprint('mol',__name__)
mols = json.load(open('./molecules.json','r'))
desc_groups = json.load(open('./descriptor_groups.json','r'))

@login_required
@mol.route('/molecules')
def index():
    return render_template('molecules/index.html',mols=mols)

@login_required
@mol.route('/molecules/<zinc_id>',methods=['GET','POST'])
def molecule_detail(zinc_id):

    if request.method == 'GET':
        sel_groups = [(g,True) for g in desc_groups]
    else:
        sel_groups = []
        for group in desc_groups:
            sel_groups.append((group,request.form.get(group)=='on'))

    return render_template('molecules/molecule_detail.html',
                           mol=mols[zinc_id],
                           molecule=zinc_id,
                           desc_groups=desc_groups,
                           sel_groups = sel_groups)