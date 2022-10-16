import datetime
from pack import db


class State(db.Model): 
    __tablename___='tbl_state'
    state_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False)
  
class User(db.Model): 
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    user_email = db.Column(db.String(255), nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_fname = db.Column(db.String(255), nullable=False)
    user_lname = db.Column(db.String(255), nullable=False)
    user_state = db.Column(db.Integer(), nullable=True)
    user_phone = db.Column(db.String(100), nullable=True)
    user_reg = db.Column(db.DateTime(), default=datetime.datetime.utcnow())


class Admin(db.Model): 
    admin_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    admin_username = db.Column(db.String(255), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    admin_lastlogin = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow())
