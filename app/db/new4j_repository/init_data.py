from returns.maybe import Maybe
import toolz as t
from operator import itemgetter
from datetime import datetime, timedelta
import uuid
from app.db.database import driver
from app.db.new4j_repository.generic import read_generic, pip_return, for_single


def device_exist(device_id):
    with driver.session() as session:
        query = """
            MATCH (d:Device {device_id: $id})
            RETURN COUNT(d) > 0 AS exists
        """
        params = {
            'id': device_id,
        }
        res = session.run(query, params).single()
        return res["exists"]


def create_device(device):
    with driver.session() as session:
        query = """
            CREATE (d:Device {
                device_id: $id,
                brand: $brand,
                model: $model,
                os: $os,
                latitude: $latitude,
                longitude: $longitude,
                altitude_meters: $altitude_meters,
                accuracy_meters: $accuracy_meters
            })
        """
        params = {
            "id": device["id"],
            "brand": device["brand"],
            "model": device["model"],
            "os": device["os"],
            "latitude": device["location"]["latitude"],
            "longitude": device["location"]["longitude"],
            "altitude_meters": device["location"]["altitude_meters"],
            "accuracy_meters": device["location"]["accuracy_meters"]
        }
        session.run(query, params)


def create_interaction_details(interaction):
    with driver.session() as session:
        query = """
            MATCH (from:Device {device_id: $from_device})
            MATCH (to:Device {device_id: $to_device})
            CREATE (from)-[r:INTERACTS_WITH {
                method: $method,
                bluetooth_version: $bluetooth_version,
                signal_strength_dbm: $signal_strength_dbm,
                distance_meters: $distance_meters,
                duration_seconds: $duration_seconds,
                timestamp: datetime($timestamp)
            }]->(to)
        """
        params = {
            "from_device": interaction["from_device"],
            "to_device": interaction["to_device"],
            "method": interaction["method"],
            "bluetooth_version": interaction["bluetooth_version"],
            "signal_strength_dbm": interaction["signal_strength_dbm"],
            "distance_meters": interaction["distance_meters"],
            "duration_seconds": interaction["duration_seconds"],
            "timestamp": interaction["timestamp"]
        }
        session.run(query, params)
