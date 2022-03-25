from utils.db import db

class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(500), nullable=False)


    def __init__(self, firstname, lastname, email, message) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message
        


    def __repr__(self) -> str:
        return f"Messages({self.id}, {self.firstname}, '{self.lastname}', '{self.message}' , '{self.email}')"
    