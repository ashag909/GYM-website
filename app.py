from flask import Flask, render_template, url_for, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import bcrypt
from models import db, User
from config import Config


# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)
# --- Forms ---
class Signupform(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


# --- Routes ---
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hashed_psw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Save to DB
        user = User(name=name, email=email, password=hashed_psw.decode("utf-8"))
        db.session.add(user)
        db.session.commit()

        flash(f"{name} registered successfully!", "success")
        return redirect(url_for("home"))
    return render_template("signup.html", form=form)

@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/membership")
def member():
    return render_template("membership.html")

@app.route("/contact")
def contacts():
    return render_template("forms.html")

@app.route("/home")
def hom():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
