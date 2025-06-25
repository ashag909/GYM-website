from flask import Flask,render_template,url_for
from flask_wtf import FlaskForm
#it is used for form velidation and managing the form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
import bcrypt


app = Flask(__name__)

class Signupform(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=StringField("Password",validators=[DataRequired()])
    submit=SubmitField("Register")



@app.route("/")
def home():
    return render_template('index.html')
@app.route("/signup")
def signup():
    form =Signupform()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password=form.password.data


        hashed_psw=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    
    render_template("signup.html")

@app.route("/Login")
def login():
    return render_template("signin.html")

@app.route("/membership")
def member():
    return render_template("membership.html")
@app.route("/contact")
def contacts():
    return render_template("forms.html")

if __name__=="__main__":
    app.run(debug=True)

    