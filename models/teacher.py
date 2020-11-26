from db import db


class TeacherModel(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    employee_id = db.Column(db.INTEGER)