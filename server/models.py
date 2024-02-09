from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True) #unique = True can be added to to make the names unique and not the same across
    created_at = db.Column(db.DateTime, server_default = db.func.now()) #when row is added to a database the time stamp will be added at the time it was added
    updated_at = db.Column(db.DateTime, onupdate = db.func.now()) #when a row is updated to a database the time stamp will be added with that time

    homeroom_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    def __repr__(self):
        return f"Name: {self.name}"

class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    teacher_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f"Name: {self.name}; Teacher Name: {self.teacher_name}"