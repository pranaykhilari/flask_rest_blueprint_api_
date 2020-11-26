from flask_restful import Resource, reqparse

from models.student import StudentModel

parser = reqparse.RequestParser()
update_parser = reqparse.RequestParser()

parser.add_argument('name', type=str, required=True, help='Name can not be blank')
parser.add_argument('email', type=str, required=True, help='Email can not be blank')
parser.add_argument('roll_no', type=int, required=True, help='Roll Number can not be blank')

update_parser.add_argument('name', type=str, help='Name can be blank')
update_parser.add_argument('email', type=str, help='Email can be blank')
update_parser.add_argument('roll_no', type=int, help='Roll Number can be blank')


class Student(Resource):

    def post(self):
        data = parser.parse_args()
        try:
            student = StudentModel.get(data.get('email'))
            if student:
                return {"Result": "{email} email id is already exists".format(email=data.get('email'))}, 409
            record = StudentModel.save_to_db(data)
            return {'Result': record}, 201
        except Exception as error:
            return {'Result': 'Error while saving record'}, 400

    def get(self, email=None):
        if email:
            student = StudentModel.get(email)
            if student:
                return {"Result": student}, 200
            return {"Result": "record not exists for {email} id".format(email=email)}, 404
        students = StudentModel.get_all()
        return {"Result": students}, 200

    def put(self, email=None):
        student = StudentModel.get_by_email(email)
        if not student:
            return {"Result": "record not exists for {email} id".format(email=email)}, 404
        data = update_parser.parse_args()
        record = StudentModel.update_student(student, data)
        return {"Result": record}, 200

    def delete(self, email=None):
        student = StudentModel.get_by_email(email)
        if student:
            record = StudentModel.delete_student(student)
            return {"Result": record}, 200
        return {"Result": "record not exists for {email} id".format(email=email)}, 404
