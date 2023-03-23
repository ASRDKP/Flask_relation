from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import Models
# from Schema import dept_schema
from views import HelloWorld, Department



app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root1234@localhost:3306/flasktaskdb'

db = SQLAlchemy(app)
# ma = Marshmallow(app)





api.add_resource(HelloWorld, '/')
api.add_resource(Department, '/Department')




if __name__ == '__main__':
    app.run(debug=True)