from flask import Flask,jsonify,request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost:5432/EmployeesInfo'
db = SQLAlchemy(app)
ma= Marshmallow(app)

class EmployeeSchema(ma.Schema):
    class Meta:
        fields= ('name','email','dob')

employees_schema = EmployeeSchema(many=True)
employee_schema = EmployeeSchema()
class Employees(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(600))
    email = db.Column(db.String(600))
    dob = db.Column(db.String(600))


