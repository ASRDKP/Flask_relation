from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from Models import Department, Employee
# from Schema import dept_schema, employee_schema
from views import HelloWorld



app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root1234@localhost:3306/flasktaskdb'

db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()



api.add_resource(HelloWorld, '/')




if __name__ == '__main__':
    app.run(debug=True)