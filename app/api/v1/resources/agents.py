# agents.py

from flask_restx import Namespace, Resource, fields

api = Namespace('agents', description='Agent related operations')

agent_model = api.model('Agent', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the agent'),
    'name': fields.String(required=True, description='The name of the agent'),
    'status': fields.String(required=True, description='The current status of the agent'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the agent was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the agent was last updated'),
})

agents = []
agent = {}

@api.route('/')
class AgentList(Resource):
    @api.marshal_list_with(agent_model)
    def get(self):
        # Lógica para listar agentes
        return agents

    @api.expect(agent_model)
    @api.marshal_with(agent_model)
    def post(self):
        # Lógica para crear un nuevo agente
        return agent
