# users.py

from flask_restx import Namespace, Resource, fields

api = Namespace('users', description='User related operations')

users = 1
user = 1

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the user'),
    'username': fields.String(required=True, description='The username of the user'),
    'password': fields.String(required=True, description='The password of the user'),
    'email': fields.String(required=True, description='The email address of the user'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the user was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the user was last updated'),
})

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        # ... your logic to get list of users
        return users

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def post(self):
        # ... your logic to create a new user
        return user

@api.route('/<int:user_id>')
class UserDetail(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        # ... your logic to get details of a user
        return user

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        # ... your logic to update a user
        return user