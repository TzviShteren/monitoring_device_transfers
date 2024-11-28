from returns.maybe import Maybe
import toolz as t
from operator import itemgetter
from datetime import datetime, timedelta
import uuid
from app.db.database import driver
# from app.db.model import Movie
# from app.db.new4j_repository.generic import read_generic, pip_return, for_single

def device_exist(device):
    with driver.session() as session:
        query = """
            MATCH (d:Device {id: $id})
            RETURN COUNT(d) > 0 AS exists
        """
        params = {
            'id': device.id,
        }
        res = session.run(query, params).single()

        return res["exists"]



def create_device(device):
    with driver.session() as session:
        query = """
            
        """
        params = {

        }
        res = session.run(query, params).single()

        return for_single(res, 'm')


def create_interaction_details(device):
    with driver.session() as session:
