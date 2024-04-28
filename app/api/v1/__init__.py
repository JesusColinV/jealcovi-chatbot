from flask import Blueprint
from flask_restx import Api, Resource, fields

# Crea el blueprint para la versión 1 de la API
api_v1 = Blueprint('api_v1', __name__, url_prefix='/v1')

# Crea una instancia de Api (opcional)
api = Api(api_v1, version='1.0', title='My ChatGPT Playground API',
          description='API para interactuar con el chatbot')



'''# Importa y registra los recursos de la API v1
from .resources import chats, documents, users, agents  # Asegúrate de que estos archivos existan

api.add_namespace(chats, path='/chats')
api.add_namespace(documents, path='/documents')
api.add_namespace(users, path='/users')
api.add_namespace(agents, path='/agents')'''


# Define el modelo de chat
chat_model = api.model('Chat', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the chat'),
    'name': fields.String(required=True, description='The name of the chat'),
    'participants': fields.List(fields.String, required=True, description='List of participants'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the chat was created'),
})

# Define el modelo de documento
document_model = api.model('Document', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the document'),
    'name': fields.String(required=True, description='The name of the document'),
    'content': fields.String(required=True, description='The content of the document'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the document was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the document was last updated'),
})

# Define el modelo de usuario
user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the user'),
    'username': fields.String(required=True, description='The username of the user'),
    'password': fields.String(required=True, description='The password of the user'),
    'email': fields.String(required=True, description='The email address of the user'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the user was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the user was last updated'),
})

# Define el modelo de agente
agent_model = api.model('Agent', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the agent'),
    'name': fields.String(required=True, description='The name of the agent'),
    'status': fields.String(required=True, description='The current status of the agent'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the agent was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the agent was last updated'),
})

# Simular datos para los recursos
chats_data = [{'id': 1, 'name': 'Chat 1', 'participants': ['user1', 'user2'], 'created_at': '2024-04-27T10:00:00'}]
documents_data = [{'id': 1, 'name': 'Document 1', 'content': 'Content of document 1', 'created_at': '2024-04-27T10:00:00', 'updated_at': '2024-04-27T10:00:00'}]
users_data = [{'id': 1, 'username': 'user1', 'password': 'password1', 'email': 'user1@example.com', 'created_at': '2024-04-27T10:00:00', 'updated_at': '2024-04-27T10:00:00'}]
agents_data = [{'id': 1, 'name': 'Agent 1', 'status': 'Active', 'created_at': '2024-04-27T10:00:00', 'updated_at': '2024-04-27T10:00:00'}]

# Definir recursos de la API

@api.route('/chats')
class ChatList(Resource):
    @api.marshal_list_with(chat_model)
    def get(self):
        return chats_data

@api.route('/documents')
class DocumentList(Resource):
    @api.marshal_list_with(document_model)
    def get(self):
        return documents_data

@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return users_data

@api.route('/agents')
class AgentList(Resource):
    @api.marshal_list_with(agent_model)
    def get(self):
        return agents_data
