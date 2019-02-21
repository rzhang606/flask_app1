from app import db
from datetime import datetime
#inherits from db.Model
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	#values inside the strings represent size, so system can optimize
	username = db.Column(db.String(64), index=True, unique = True)
	email = db.Column(db.String(120), index=True, unique = True)
	password_hash = db.Column(db.String(128))

	#new posts field, backref defines the name of field added to "many" class that 
	#points back to the "one" object (Posts -> users)
	posts = db.relationship('Post', backref='author', lazy = 'dynamic')

	#tells python how to print objects of this class (__repr__)
	def __repr__(self):
		return  '<User {}>'.format(self.username) #Output: <User 'name'>


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #passing the function itself
	#the foreign key, connects the tables in db
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)
