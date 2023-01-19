from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from startup import db, get_user, User
import bcrypt as bc


def getPassword(username, password):
	query = get_user()
	print(query)
	for i in query:
		word = i.username
		if(word == username):
			hashed = bc.hashpw(bytes(password, "utf-8"),i.salt)
			return hashed, i.password
		return "404","wrong user"
	

def putInDatabase(request,login, password, mail, saltGen):
    if request.method == 'POST':
        user_to_register = User(
                               username = login,
                               password = password,
                               email = mail,
                               salt = saltGen
                              )

        db.session.add(user_to_register)
        db.session.commit()
