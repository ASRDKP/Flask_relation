from app import db, app


class Department(db.Model):
    __tablename__ = 'department'
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            'dept_id'   : self.dept_id,
            'dept_name' : self.dept_name
        }



# class Employee(db.Model):
#     __tablename__ = 'employee'
#     empid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     surname = db.Column(db.String(50), nullable=False)
#     dept_id = db.Column(db.Integer, db.ForeignKey('dept_id'), nullable=False)
#     postion = db.Column(db.String(35), nullable=False)
#     email = db.Column(db.String(75), unique=True, nullable=False)
#     salary = db.Column(db.Integer, nullable=False)
#     contact = db.Column(db.Integer(10), nullable=False)
#     deptartment = db.relationship("Department", backref="employees")
    
    
#     def serialize(self):
#         return{
#             'id'      : self.id,
#             'name'    : self.name,
#             'surname' : self.surname,
#             'dept_id' : self.dept_id,
#             'postion' : self.postion,
#             'email'   : self.email,
#             'salary'  : self.salary,
#             'contact' : self.contact,
#         }



with app.app_context():
    db.create_all()