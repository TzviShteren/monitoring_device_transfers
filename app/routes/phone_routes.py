from flask import Blueprint, jsonify, request
from app.service.set_data import *
phone_blueprint = Blueprint('phone_tracker', __name__)


@phone_blueprint.route("/", methods=['POST'])
def get_interaction():
    # print(request.json, index=4)
    normalization_to_new4j(request.json)
    return jsonify({}), 200
