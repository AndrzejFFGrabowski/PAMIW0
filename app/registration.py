from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import os

login_manager = LoginManager()


#def init(app):
JWT_SECRET = os.getenv("JWT_SECRET")
app.config['SECRET_KEY'] = JWT_SECRET
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	#login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db = SQLAlchemy(App)

class User(db.Model, UserMixin):
    tablename = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(254))
    email = db.Column(db.String(254))
    salt = db.Column(db.String(254))

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/register', methods = ['GET', 'POST'])
def register():

    login = request.form.get("login", "")
    password = request.form.get("password", "")
    rpassword = request.form.get("rpassword", "")
    email_address = request.form.get("email", "")

    if request.method == 'POST':
        if not login or not password or not rpassword or not email_address:
            flash('You must fill all fields!')
            return redirect(request.url)

        if password != rpassword:
            flash('Given passwords are not the same!')
            return redirect(request.url)

        if len(password) and len(rpassword) < 8:
            flash('Password too short. Minimum 8 characters are required!')
            return redirect(request.url)

        if len(login) < 4:
            flash('Login too short. Minimum 4 characters are required!')
            return redirect(request.url)

        if len(email_address) < 3:
            flash('Email too short. Minimum 3 characters are required!')
            return redirect(request.url)

        login_validation = User.query.filter_by(username = login).first()

        if login_validation:
            flash("Given login is already taken!")
            return redirect(request.url)

        email_validation = User.query.filter_by(email = email_address).first()

        if email_validation:
            flash("Given email address is already taken!")
            return redirect(request.url)

        hashed_password, salt_1 = hash_password(password, '1')
        user_to_register = User(
                               username = login,
                               password = hashed_password,
                               email = email_address,
                               salt = salt_1
                              )

        db.session.add(user_to_register)
        db.session.commit()
        return redirect("/forms")

#return render_template('register.html')
