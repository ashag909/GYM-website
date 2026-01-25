from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import bcrypt


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def check_password(self,password):
       return bcrypt.checkpw(password.encode('utf-8'),
                          self.password.encode('utf-8'))

    def __repr__(self):
        return f"<User {self.full_name}>"
