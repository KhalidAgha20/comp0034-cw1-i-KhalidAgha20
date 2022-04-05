from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myflask import db


class User(db.Model, UserMixin):
    # __table__ = db.Model.metadata.tables['user']

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    user_type = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.DOB} {self.email} {self.username} {self.password} \
        {self.country} {self.user_type}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



