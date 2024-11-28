from flask import Blueprint, jsonify, request
from app.db.new4j_repository.connected_repository import *

connected_blueprint = Blueprint('connected', __name__)


@connected_blueprint.route('/bluetooth-connections', methods=['GET'])
def get_bluetooth_connections():
    res = calls_with_bluetooth()
    return jsonify(res), 200


@connected_blueprint.route('/bluetooth_signal_strength_stronger_than_60', methods=['GET'])
def signal_strength_dbm_stronger_than_60():
    res = signal_strength_stronger_than_60()
    return jsonify(res), 200


@connected_blueprint.route('/how_many_called_the_device', methods=['GET'])
def how_many_called_the_device():
    device_id = request.args.get('device_id')

    if device_id is None:
        return jsonify({'error': 'No device id'}), 400

    res = how_many_called_the_device_by_id(device_id)

    return jsonify(res), 200


@connected_blueprint.route('/device_direct_connection', methods=['GET'])
def check_direct_connection():
    device_id_1 = request.args.get('device_id_1')
    device_id_2 = request.args.get('device_id_2')

    if not device_id_1 or not device_id_2:
        return jsonify({"error": "Both device_id_1 and device_id_2 are required"}), 400

    is_connected = check_direct_connection_by_id(device_id_1, device_id_2)

    return jsonify({
        "device_id_1": device_id_1,
        "device_id_2": device_id_2,
        "direct_connection": is_connected
    }), 200


@connected_blueprint.route('/most_recent_interaction', methods=['GET'])
def most_recent_interaction():
    device_id = request.args.get('device_id')
    if device_id is None:
        return jsonify({'error': 'No device id'}), 400

    res = most_recent_interaction_by_id(device_id)

    return jsonify(res), 200
