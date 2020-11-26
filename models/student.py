from db import db, marshmallow


class StudentModel(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    roll_no = db.Column(db.INTEGER)

    @classmethod
    def save_to_db(cls, data):
        student = cls(
            name=data.get('name'),
            email=data.get('email'),
            roll_no=data.get('roll_no')
        )
        db.session.add(student)
        db.session.commit()
        return student_schema.dump(student)

    @classmethod
    def get(cls, email):
        student = cls.query.filter(cls.email == email).first()
        return student_schema.dump(student)

    @classmethod
    def get_by_email(cls, email):
        student = cls.query.filter(cls.email == email).first()
        return student

    @classmethod
    def get_all(cls):
        students = cls.query.all()
        return students_schema.dump(students)

    @classmethod
    def update_student(cls, student, data):
        for key, value in data.items():
            if value:
                setattr(student, key, value)
        db.session.commit()
        return student_schema.dump(student)

    @staticmethod
    def delete_student(student):
        db.session.delete(student)
        db.session.commit()
        return student_schema.dump(student)


class StudentSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'roll_no')
        model = StudentModel


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
