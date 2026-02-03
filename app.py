from flask import Flask, render_template, url_for, request, flash, redirect
from models import db, User
from config import Config
from forms import LoginForm, Signupform
from flask_login import login_user,current_user,LoginManager,login_required
import os 
import bcrypt
# Initialize app
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Ilovemyfamily%40143@localhost/gymdb'
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY','dev-secret')
app.config.from_object(Config)

# Initialize database

db.init_app(app)


login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'


# --- Routes ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
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

        '''hashed_psw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Save to DB
        user=User.query.filter_by(email=form.username.data).first()
        db.session.add(user)
        db.session.commit()

        flash(f"{name} registered successfully!", "success")
        return redirect(url_for("home"))
    return render_template("signup.html", form=form)'''
        existing_user=User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered. Please login.")
            return redirect(url_for("login"))
        
        hashed_psw=bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        
        user=User(
            full_name=name,
            email=email,
            password=hashed_psw
        )
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully! Please login.","Success")
        return redirect(url_for('login'))
    return render_template("signup.html",form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
       user=User.query.filter_by(email=form.username.data).first()
       if user is None or not user.check_password(form.password.data):
           flash("Invalid username or password")
           return redirect(url_for('login'))
       login_user(user, remember=form.remember_me.data)
       next_page=request.args.get('next')
       return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template("signin.html",title='Sign In',form=form)

@app.route("/membership")
@login_required
def member():
    return render_template("membership.html")

@app.route("/contact")
def contacts():
    return render_template("forms.html")




@app.route("/about")
def about():
    return render_template("about.html")







if __name__ == "__main__":
    app.run(debug=True)
