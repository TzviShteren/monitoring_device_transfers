from flask import Blueprint, jsonify, request

# from analysis_serviceapp.db.new4j_repository import movie_repository as mr

analysis_blueprint = Blueprint('analysis', __name__)


@analysis_blueprint.route('/patterns', methods=['GET'])
def get_patterns():
    pass


@analysis_blueprint.route('/hotspots', methods=['GET'])
def get_hotspots():
    pass


@analysis_blueprint.route('/networks', methods=['GET'])
def get_networks():
    pass
