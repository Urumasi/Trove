"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, redirect, json
from .forms import LogUserForm, dropForm, cenyForm
from ..data.database import db
from ..data.models import LogUser, drop, cenyd, den
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/data-input', methods=['GET', 'POST'])
def data_input():
    form = dropForm()
    if form.validate_on_submit():
        drop.create(**form.data)
        return redirect('/data-input')
    pole = db.session.query(drop).all()
    archived = db.session.query(den).all()
    cenydata = db.session.query(cenyd).order_by('-id').first()
    ceny = []
    cenya = []
    sums = {'flux':0, 'eye':0, 'cache':0, 'chest':0, 'twice':0, 'thrice':0, 'quad':0, 'penta':0, 'all':0}
    sumsa = {'flux':0, 'eye':0, 'cache':0, 'chest':0, 'twice':0, 'thrice':0, 'quad':0, 'penta':0, 'all':0}
    if cenydata==None:
        for n in pole:
            ceny.append('-')
        for n in archived:
            cenya.append('-')
    else:
        for n in pole:
            cena = n.flux
            sums['flux'] += n.flux
            cena += n.eye * cenydata.eye
            sums['eye'] += n.eye
            cena += n.cache * cenydata.cache
            sums['cache'] += n.cache
            cena += n.chest * cenydata.chest
            sums['chest'] += n.chest
            cena += n.twice * cenydata.twice
            sums['twice'] += n.twice
            cena += n.thrice * cenydata.thrice
            sums['thrice'] += n.thrice
            cena += n.quad * cenydata.quad
            sums['quad'] += n.quad
            cena += n.penta * cenydata.penta
            sums['penta'] += n.penta
            ceny.append(cena)
            sums['all'] += cena
        for n in archived:
            cena = n.flux
            sumsa['flux'] += n.flux
            cena += n.eye * cenydata.eye
            sumsa['eye'] += n.eye
            cena += n.cache * cenydata.cache
            sumsa['cache'] += n.cache
            cena += n.chest * cenydata.chest
            sumsa['chest'] += n.chest
            cena += n.twice * cenydata.twice
            sumsa['twice'] += n.twice
            cena += n.thrice * cenydata.thrice
            sumsa['thrice'] += n.thrice
            cena += n.quad * cenydata.quad
            sumsa['quad'] += n.quad
            cena += n.penta * cenydata.penta
            sumsa['penta'] += n.penta
            cenya.append(cena)
            sumsa['all'] += cena
    return render_template('public/data-input.tmpl', form=form, data=pole, enumerate=enumerate, ceny=ceny, sums=sums, archived=archived, sumsa=sumsa, cenya=cenya)

@blueprint.route('/data-delete/<int:id>')
def data_delete(id):
    pole = db.session.query(drop).filter_by(id=id).first()
    db.session.delete(pole)
    db.session.commit()
    return redirect('/data-input')

@blueprint.route('/ceny-input', methods=['GET', 'POST'])
def ceny_input():
    form = cenyForm()
    pole = db.session.query(cenyd).all()
    if form.validate_on_submit():
        print form.data
        cenyd.create(**form.data)
        return redirect('/ceny-input')
    return render_template('public/ceny-input.tmpl', form=form, enumerate=enumerate, data=pole, num=pole.__len__())

@blueprint.route('/ceny-pouzit/<int:id>;<int:a>;<int:b>;<int:c>;<int:d>;<int:e>;<int:f>;<int:g>', methods=['GET', 'POST'])
def ceny_input2(a, b, c, d, e, f, g):
    dt = {'eye':a, 'cache':b, 'chest':c, 'twice':d, 'thrice':e, 'quad':f, 'penta':g}
    cenyd.create(**dt)
    return redirect('/ceny-delete/'+str(id))

@blueprint.route('/ceny-delete/<int:id>')
def ceny_delete(id):
    pole = db.session.query(cenyd).filter_by(id=id).first()
    db.session.delete(pole)
    db.session.commit()
    return redirect('/ceny-input')

@blueprint.route('/data-archive/<com>/<idsstr>')
def data_archive(com, idsstr):
    ids = json.loads(idsstr)
    npole = {'flux':0, 'eye':0, 'cache':0, 'chest':0, 'twice':0, 'thrice':0, 'quad':0, 'penta':0, 'comment':com}
    for n in ids:
        pole = db.session.query(drop).filter_by(id=n).first()
        npole['flux'] += pole.flux
        npole['eye'] += pole.eye
        npole['cache'] += pole.cache
        npole['chest'] += pole.chest
        npole['twice'] += pole.twice
        npole['thrice'] += pole.thrice
        npole['quad'] += pole.quad
        npole['penta'] += pole.penta
        db.session.delete(pole)
        db.session.commit()
    den.create(**npole)
    return redirect('/data-input')