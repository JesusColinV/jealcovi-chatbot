# documents.py

from flask_restx import Namespace, Resource, fields

api = Namespace('documents', description='Document related operations')

document_model = api.model('Document', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the document'),
    'name': fields.String(required=True, description='The name of the document'),
    'content': fields.String(required=True, description='The content of the document'),
    'created_at': fields.DateTime(readOnly=True, description='The date and time when the document was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The date and time when the document was last updated'),
})

documents = 1
document = 1

@api.route('/')
class DocumentList(Resource):
    @api.marshal_list_with(document_model)
    def get(self):
        # ... your logic to get list of documents
        return documents

    @api.expect(document_model)
    @api.marshal_with(document_model)
    def post(self):
        # ... your logic to create a new document
        return document

@api.route('/<int:document_id>')
class DocumentDetail(Resource):
    @api.marshal_with(document_model)
    def get(self, document_id):
        # ... your logic to get a specific document
        return document

    @api.expect(document_model)
    @api.marshal_with(document_model)
    def put(self, document_id):
        # ... your logic to update a specific document
        return document

    def delete(self, document_id):
        # ... your logic to delete a specific document
        return '', 204