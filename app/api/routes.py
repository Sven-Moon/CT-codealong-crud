
from flask import Blueprint, jsonify
from app.models import Animal

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/test', methods=['GET'])
def test():
    fox = Animal.query.all()[0]
    return jsonify(fox.to_dict()), 200