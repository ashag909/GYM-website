from flask import Flask,render_template
from flask_wtf import FlaskForm
#it is used for form velidation and managing the form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError



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
    
    render_template("signup.html")

@app.route("/login")
def login():
    render_template("signin.html")

@app.route("/membership")
def member():
    render_template("forms.html")

if __name__=="__main__":
    app.run(debug=True)

    