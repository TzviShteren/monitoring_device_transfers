from returns.maybe import Maybe
import toolz as t
from operator import itemgetter
from app.db.database import driver


def calls_with_bluetooth():
    with driver.session() as session:
        query = """
            MATCH (d1:Device)-[r:INTERACTS_WITH]->(d2:Device)
            WHERE r.method = 'Bluetooth'
            RETURN d1, d2
        """
        res = session.run(query).data()
        return res


def signal_strength_stronger_than_60():
    with driver.session() as session:
        query = """
            MATCH (d1:Device)-[r:INTERACTS_WITH]->(d2:Device)
            WHERE r.signal_strength_dbm > -60
            RETURN d1, d2
        """
        res = session.run(query).data()
        return res


def how_many_called_the_device_by_id(device_id) -> int:
    with driver.session() as session:
        query = """
            MATCH (d:Device)-[:INTERACTS_WITH]->(d1:Device)
            WHERE d.device_id = $device_id
            RETURN COUNT(d1)
        """
        params = {
            "device_id": device_id,
        }
        res = session.run(query, params).single()
        return res


def check_direct_connection_by_id(device_id_1, device_id_2):
    with driver.session() as session:
        query = """
            MATCH (d1:Device)-[:INTERACTS_WITH]->(d2:Device)
            WHERE d1.device_id = $device_id_1 AND d2.device_id = $device_id_2
            RETURN COUNT(*) > 0 AS is_connected
        """

        params = {
            "device_id_1": device_id_1,
            "device_id_2": device_id_2
        }

        res = session.run(query, params).single()

        return res
