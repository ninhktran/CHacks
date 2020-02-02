from Website import db

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    area = db.Column(db.String(120),nullable=False)
    topic = db.Column(db.String(120), nullable=False)
    # everett = db.Column(db.Boolean(), default=False)
    # skagit_county = db.Column(db.Boolean(), default=False)
    # weather = db.Column(db.Boolean(), default=False)
    # sports = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.area}', '{self.topic}')"

    def get_area(self):
        return self.area

    def get_topic(self):
        return self.topic


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.email}')"

