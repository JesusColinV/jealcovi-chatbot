from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/hello')
def hello_world():
    return jsonify({'message': 'Hola Mundo!'})