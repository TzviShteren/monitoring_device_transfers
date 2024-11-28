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


def process_devices_and_interaction(device_1, device_2, interaction):
    with driver.session() as session:
        # Create device query
        query_create_device = """
            MERGE (d1:Device {device_id: $id1})
            ON CREATE SET 
                d1.brand = $brand1,
                d1.model = $model1,
                d1.os = $os1,
                d1.latitude = $latitude1,
                d1.longitude = $longitude1,
                d1.altitude_meters = $altitude_meters1,
                d1.accuracy_meters = $accuracy_meters1
            
            MERGE (d2:Device {device_id: $id2})
            ON CREATE SET 
                d2.brand = $brand2,
                d2.model = $model2,
                d2.os = $os2,
                d2.latitude = $latitude2,
                d2.longitude = $longitude2,
                d2.altitude_meters = $altitude_meters2,
                d2.accuracy_meters = $accuracy_meters2
        """

        # Create interaction query
        query_create_interaction = """
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

        # Check and create device_1
        if not session.run(query_check_device, {'id': device_1['id']}).single()['exists']:
            session.run(query_create_device, {
                "id": device_1["id"],
                "brand": device_1["brand"],
                "model": device_1["model"],
                "os": device_1["os"],
                "latitude": device_1["location"]["latitude"],
                "longitude": device_1["location"]["longitude"],
                "altitude_meters": device_1["location"]["altitude_meters"],
                "accuracy_meters": device_1["location"]["accuracy_meters"]
            })
            print()

        # Check and create device_2
        if not session.run(query_check_device, {'id': device_2['id']}).single()['exists']:
            session.run(query_create_device, {
                "id": device_2["id"],
                "brand": device_2["brand"],
                "model": device_2["model"],
                "os": device_2["os"],
                "latitude": device_2["location"]["latitude"],
                "longitude": device_2["location"]["longitude"],
                "altitude_meters": device_2["location"]["altitude_meters"],
                "accuracy_meters": device_2["location"]["accuracy_meters"]
            })

        # Create the interaction
        session.run(query_create_interaction, {
            "from_device": interaction["from_device"],
            "to_device": interaction["to_device"],
            "method": interaction["method"],
            "bluetooth_version": interaction["bluetooth_version"],
            "signal_strength_dbm": interaction["signal_strength_dbm"],
            "distance_meters": interaction["distance_meters"],
            "duration_seconds": interaction["duration_seconds"],
            "timestamp": interaction["timestamp"]
        })
