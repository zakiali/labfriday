from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    lunches = db.relationship('Lunches', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<Nickname: {0}> <Email: {1}>'.format(self.nickname, self.email)


class Lunches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String(50))
    datestamp = (db.Column(db.Date))
    order = db.Column(db.String(200))
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Author: {0}> <Restaurant: {1}> <Datestamp: {2}> <Order: {3}> <Price: {4}>'.format(self.author, self.restaurant, self.datestamp, self.order, self.price)
