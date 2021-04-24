from studentcompanion import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    number = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    to_list = db.relationship('Todo', back_populates='user', lazy=True)
    tt = db.relationship('Timetable', backref='user', lazy=True)
    rem = db.relationship('Reminders',backref='user',lazy=True)
    def __repr__(self):
        return f"User('{self.name}','{self.email}')"


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_item = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='to_list', lazy=True)


class Timetable(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    time_table = db.Column(db.PickleType,default=[['Monday','','','','','','','','','','','',''],
                                                  ['Tuesday','','','','','','','','','','','',''],
                                                  ['Wednesday','','','','','','','','','','','',''],
                                                  ['Thursday','','','','','','','','','','','',''],
                                                  ['Friday','','','','','','','','','','','',''],
                                                  ['Saturday','','','','','','','','','','','',''],
                                                  ['Sunday','','','','','','','','','','','','']])


class Reminders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    event = db.Column(db.Text,nullable=False)
    date_time = db.Column(db.String(16), nullable=False)
    number = db.Column(db.String(10),nullable=False)
