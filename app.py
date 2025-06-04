from flask import Flask,render_template
from flask_wtf import FlaskForm
#it is used for form velidation and managing the form



app = Flask(__name__)






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

    