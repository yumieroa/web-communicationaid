
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect
from sqlalchemy import *
from model import Parent, Child, Account, db
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def mode():
    return render_template('mode.html')
@app.route('/user/<acc_id>', methods=['GET'])
def getoneuser(acc_id):
    user = Account.query.filter_by(acc_id=acc_id).first()
    if not user:
        return jsonify({'message: "no user found"'})
    user_data = {}
    user_data['acc_id'] = user.acc_id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['acc_type'] = user.acc_type
    return jsonify({'user': user_data})

@app.route('/parent/<acc_id>', methods=['GET'])
def parent(acc_id):
    myParent = Parent.query.filter_by(p_id=acc_id)
    # return jsonify({'message': 'Successfully updated!'})
    return render_template('p_prof.html', myParent=myParent)

@app.route('/edit_parent/<acc_id>', methods=['GET','POST'])
def edit_parent(acc_id):
    if request.method == "POST":
        new_parent = Parent(request.form['fname_p'], request.form['lname_p'], request.form['bday_p'], request.form['add_p']).where(p_id=acc_id)
    # if request.method == "PUT":
    #     new_parent = update(Parent).where(acc_id==1). \
    #         values(fname_p=request.form['fname_p'])
        db.session.add(new_parent)
        db.session.commit()
        print "hello"
        return redirect('/parent/<acc_id>')
    if request.method == "GET":
        return render_template('edit_p.html')

@app.route('/del_parent', methods=['GET','POST'])
def del_parent():
    if request.method == "POST":
        del_p = Parent.query.all()
        db.session.delete(del_p)
        db.session.commit()
        print "hello"
        return redirect('/parent')

@app.route('/child', methods=['GET'])
def child():
    myChild = Child.query.all()
    return render_template('c_prof.html', myChild=myChild)

@app.route('/edit_child', methods=['GET','POST'])
def edit_child():
    if request.method == "POST":
        child = Child(request.form['fname_c'], request.form['lname_c'], request.form['bday_c'], request.form['diagnosis'])
        db.session.add(child)
        db.session.commit()
        print "hello"
        return redirect('/child')
    if request.method == "GET":
        return render_template('edit_c.html')


# @app.route('/edit_parent', method=['POST'])
# def edit_parent():


if __name__ == "__main__":
    app.run(debug=True)