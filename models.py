from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    hashSalt = db.Column(db.Binary(120))
    hashpwd = db.Column(db.Binary(120))

    blogs = db.relationship('Blogs', backref='owner')

    def __init__(self, username, hashSalt, hashpwd):
        self.username = username
        self.hashSalt = hashSalt
        self.hashpwd = hashpwd


class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __init__(self, title, body, owner_id):
        self.title = title
        self.body = body
        self.owner_id = owner_id
