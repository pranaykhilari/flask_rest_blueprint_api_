from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask:flask@123@localhost:5432/flaskdb"

from urls import url

url(app)

from models.teacher import TeacherModel
from models.student import StudentModel

if __name__ == '__main__':
    app.run(debug=True)
