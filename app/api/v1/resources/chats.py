# chat.py (example)

from flask_restx import Namespace, Resource

api = Namespace('chat', description='Chat related operations')

@api.route('/')
class ChatList(Resource):
    def get(self):
        # ... your logic to get list of chats
        return 1

@api.route('/<int:chat_id>')
class Chat(Resource):
    def get(self, chat_id):
        # ... your logic to get a specific chat
        return 1