import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','dev-secret')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ilovemyfamily%40143@localhost/gymdb' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

