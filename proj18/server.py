from flask import Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect
from model import Parent, Child, Account, db


server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
server.config['SECRET_KEY'] = 'hard to guess string'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(server)

@server.route('/parent', methods=['GET'])
def parent():
	if request.method == 'POST':
        return render_template('p_prof.html', myParent=myParent)