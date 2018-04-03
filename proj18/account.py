
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import Parent, Child, Account, db
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def welcome():
    return render_template('welcome.html')


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

@app.route('/mode/<int:acc_id>')
def mode(acc_id):
    return render_template('mode.html', acc_id=int(acc_id))

@app.route('/parent_mode/<int:acc_id>')
def parent_mode(acc_id):
    return render_template('p_mode.html', acc_id=int(acc_id))

@app.route('/navigation')
def nav():
    return render_template('navigation.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/toys')
def toys():
    return render_template('toys.html')

@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/parent/<int:acc_id>', methods=['GET'])
def parent(acc_id):
    myParent = Parent.query.filter_by(acc_id=int(acc_id)).all()
    # return jsonify({'message': 'Successfully updated!'})
    return render_template('p_prof.html', myParent=myParent)

@app.route('/edit_parent/<int:acc_id>', methods=['GET','POST'])
def edit_parent(acc_id):
    myParent = Parent.query.filter_by(acc_id=int(acc_id)).first()

    if request.method == "POST":

        myParent.fname_p = request.form['fname_p']
        myParent.lname_p = request.form['lname_p']
        myParent.bday_p = request.form['bday_p']
        myParent.add_p = request.form['add_p']

        myParent = db.session.merge(myParent)
        db.session.add(myParent)
        db.session.commit()
        print "hello success"
        return redirect(url_for('parent', acc_id=int(acc_id)))

    if request.method == "GET":
        return render_template('edit_p.html', acc_id=int(acc_id))


@app.route("/upload_parent", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("p_prof.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/child/<int:p_id>', methods=['GET'])
def child(p_id):
    myChild = Child.query.filter_by(p_id=int(p_id)).all()
    # return jsonify({'message': 'Successfully updated!'})
    return render_template('c_prof.html', myChild=myChild)

@app.route('/edit_child/<int:p_id>', methods=['GET','POST'])
def edit_child(p_id):
    myChild = Child.query.filter_by(p_id=int(p_id)).first()

    if request.method == "POST":

        myChild.fname_c = request.form['fname_c']
        myChild.lname_c = request.form['lname_c']
        myChild.bday_c = request.form['bday_c']
        myChild.diagnosis = request.form['diagnosis']

        myChild = db.session.merge(myChild)
        db.session.add(myChild)
        db.session.commit()
        print "hello success"
        return redirect(url_for('child', p_id=int(p_id)))

    if request.method == "GET":
        return render_template('edit_c.html', p_id=int(p_id))

# @app.route('/edit_parent', method=['POST'])
# def edit_parent():


if __name__ == "__main__":
    app.run(threaded=True)