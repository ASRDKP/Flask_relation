# from app import ma
from app import app
from Models import Department
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class dept_schema(ma.SQLAlchemySchema):
    class Meta:
        model : Department
        
    dept_id   = ma.auto_field()
    dept_name = ma.auto_field()
        
        
# class employee_schema(ma.SQLAlchemySchema):
#     class Meta:
#         model : Employee
        
#     empid = ma.auto_field()
#     name = ma.auto_field()
#     surname = ma.auto_field()
#     dept_id = ma.auto_field()
#     postion = ma.auto_field()
#     email = ma.auto_field()
#     salary = ma.auto_field()
#     contact = ma.auto_field()