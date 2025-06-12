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

