from flask import Blueprint, jsonify, request

movements_blueprint = Blueprint('movements', __name__)


# {
#     "device_id": "D12345",
#     "owner_id": "314894775",
#     "timestamp": "2023-10-15T14:30:00Z",
#     "location": {
#     "location_id": "L67890",
#     },
#     "movement_type": "vehicle",
#     "confidence_level": 0.95
# }
@movements_blueprint.route('/', methods=['POST'])
def create_movement():
    data = request.get_json()
    if not all(
            x in data for x in ('device_id', 'owner_id', 'timestamp', 'location', 'movement_type', 'confidence_level')):
        return jsonify({"error": "Missing required fields"}), 400


@movements_blueprint.route('/<movements>', methods=['GET'])
def get_movements(movements):
    try:
        pass

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@movements_blueprint.route('/search', methods=['GET'])
def search_movements():
    pass


@movements_blueprint.route('/<device_id>/history', methods=['GET'])
def history_movements():
    pass
