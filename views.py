from flask_restful import Resource
# from Models import Department
# from Schema import dept_schema


class HelloWorld(Resource):
    def get(self):
        return {
            'data' : 'The app is working Fine for now.'
        }
        
        
# class Department(Resource):
#     def get(self):
#         try:
#             print("Inside the Get department")
#             data = Department.query.all()
            
#         except Exception as e:
#             df = {
#                 "Error_Status" : "404 Bad Request",
#                 "Error_Message" : e.args[0]
#             }
#             print("Error : ", e.args[0])
            
#             return df            