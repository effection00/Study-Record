from twit_app import db

class User(db.Model):
    __tablename__ = ''

    id = db.Column(db.Integer())

    def __repr__(self):
        return f"User {self.id}"
