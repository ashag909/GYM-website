import os

class Config:
    SECRET_KEY = "yuerbdsbnvyufv"
    SQLALCHEMY_DATABASE_URI = "sqlite:///gym.db"  # or MySQL/Postgres
    SQLALCHEMY_TRACK_MODIFICATIONS = False
