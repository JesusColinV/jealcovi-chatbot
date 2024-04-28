# ./app/api/__init__.py

from flask import Blueprint
from .v1 import api_v1


api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(api_v1)

