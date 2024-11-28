from flask import Blueprint, jsonify, request

# from analysis_serviceapp.db.new4j_repository import movie_repository as mr

intelligence_blueprint = Blueprint('intelligence', __name__)


@intelligence_blueprint.route('/locations/ranking', methods=['GET'])
def locations_ranking():
    pass


@intelligence_blueprint.route('/persons/ranking', methods=['GET'])
def persons_ranking():
    pass


@intelligence_blueprint.route('/predictions', methods=['GET'])
def predictions():
    pass
