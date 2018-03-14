from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/proj'
db = SQLAlchemy(app)

# relationship between specifics and logs
activity = db.Table('activity',
                    db.Column('spec_num', db.Integer, db.ForeignKey('specifics.spec_num')),
                    db.Column('log_num', db.Integer, db.ForeignKey('logs.log_num'))
                    )
report = db.Table('report',
                    db.Column('item_num', db.Integer, db.ForeignKey('items.item_num')),
                    db.Column('prog_num', db.Integer, db.ForeignKey('progress.prog_num'))
                  )


class Account(db.Model):
    acc_id = db.Column(db.Integer, primary_key=True)
    acc_type = db.Column(db.String(20), unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), unique=True)
class Access_Token(db.Model):
    token_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(20), unique=True)
class Parent(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    fname_p = db.Column(db.String(80))
    lname_p = db.Column(db.String(80))
    bday_p = db.Column(db.Date)
    add_p = db.Column(db.String(120))
class Child(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    fname_c = db.Column(db.String(80))
    lname_c = db.Column(db.String(80))
    bday_c = db.Column(db.Date)
    diagnosis = db.Column(db.String(50))
    pers = db.relationship('Personal', backref='child', lazy='dynamic')
class Teacher(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    fname_t = db.Column(db.String(80))
    lname_t = db.Column(db.String(80))
    bday_t = db.Column(db.Date)
    specialty = db.Column(db.String(120))
    tel_num = db.Column(db.BigInteger)
    add_t = db.Column(db.String(120))
class Personal(db.Model):
    per_num = db.Column(db.Integer, primary_key=True)
    per_name = db.Column(db.String(50))
    child_id = db.Column(db.Integer, db.ForeignKey('child.c_id'))
    spec = db.relationship('Specifics', backref='specify', lazy='dynamic')
class Specifics(db.Model):
    spec_num = db.Column(db.Integer, primary_key=True)
    spec_name = db.Column(db.String(50)),
    act = db.relationship('Activities', secondary=activity, backref=db.backref('act', lazy='dynamic'))
    specify_id = db.Column(db.Integer, db.ForeignKey('personal.per_num'))
class Logs(db.Model):
    log_num = db.Column(db.Integer, primary_key=True)
    clicks = db.Column(db.Integer)
    log_date = db.Column(db.Date)
    log_time = db.Column(db.Time)
class Class(db.Model):
    class_num = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))
    ed = db.relationship('Educational', backref='edu', lazy='dynamic')
class Educational(db.Model):
    ed_num = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    edu_id = db.Column(db.Integer, db.ForeignKey('class.class_num'))
class Items(db.Model):
    item_num = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(120)),
    rep = db.relationship('Report', secondary=report, backref=db.backref('rep', lazy='dynamic'))
class Progress(db.Model):
    prog_num = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(500))
    prog_date = db.Column(db.Date)
    prog_time = db.Column(db.Time)
    score = db.Column(db.Integer)
class Images(db.Model):
    img_id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(50))
class Audio(db.Model):
    aud_id = db.Column(db.Integer, primary_key=True)
    aud = db.Column(db.String(50))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
