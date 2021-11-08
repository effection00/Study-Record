from twit_app import db

class Tweet(db.Model):
    __tablename__ = ''

    id = db.Column(db.Integer())

    def __repr__(self):
        return f"Tweet {self.id}"
