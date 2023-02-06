from models import *


@app.route('/employees',methods=['GET'])
def get_employees():
    employees_data = Employees.query.all()
    result = employees_schema.dump(employees_data)
    return jsonify(result)
  

@app.route('/updateemployee/<id>',methods=['GET','POST'])
def get_employee(id):
  employee_data = Employees.query.get(id)
  name= request.form.get('name')
  email = request.form.get('email')
  dob = request.form.get('dob')
  employee_data.name = name
  employee_data.email = email
  employee_data.dob = dob
  db.session.commit()
  result = employee_schema.dump(employee_data)
  return jsonify(result)

@app.route('/deleteemployee/<id>',methods=['GET'])
def delete_employee(id):
    current_employee = Employees.query.get(id)
    db.session.delete(current_employee)
    db.session.commit()
    return 'employee deleted sucessfully'






if __name__ == '__main__':
    app.run()