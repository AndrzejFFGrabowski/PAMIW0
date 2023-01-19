from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from startup import db, get_user, User

count =0

def getPassword(username):
	query = get_user()
	print(query)
	for i in query:
		word = i.username
		if(word == username):
			return i.password
		return "wrong user"
	

def putInDatabase(request):
    login = request.form.get("login", "")
    password = request.form.get("password", "")
    rpassword = request.form.get("rpassword", "")
    email_address = request.form.get("email", "")

    if request.method == 'POST':
        #hashed_password  = bcrypt.hashpw(password,"a")
        user_to_register = User(
                               username = login,
                               password = password,
                               email = email_address,
                               salt = "a"
                              )

        db.session.add(user_to_register)
        db.session.commit()
