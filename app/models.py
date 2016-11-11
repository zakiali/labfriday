from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    lunches = db.relationship('Lunches', backref='author', lazy='dynamic')
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property 
    def is_anononymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Lunches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String(50))
    datestamp = (db.Column(db.Date))
    order = db.Column(db.String(200))
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Restaurant %r>' % (self.restaurant)
