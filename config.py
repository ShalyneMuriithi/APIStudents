# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/learners_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
