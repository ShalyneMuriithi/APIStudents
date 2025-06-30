# app/models.py

from . import db

class Learners(db.Model):
    __tablename__ = "school_learners"
    school_id = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.Integer)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    course_name = db.Column(db.String(1000))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    county = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)







# endpoints
#- register
#- login
#- user profile


#- hash password
#- login - jwt token(refresh token)
#- userprofile - protected; Authorization: Bearer token
#- logout - token expire, press logout (expire token, delete)