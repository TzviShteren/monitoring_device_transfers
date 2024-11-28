from app.db.new4j_repository.init_data import *
from app.db.new4j_repository.device_repository import set_device_location


def normalization_to_new4j(data):
    for interaction in data:
        devices = interaction["devices"]
        interaction_details = interaction["interaction"]
        for device in devices:
            if device_exist(device):
                set_device_location(device)
            create_device(device)
        create_interaction_details(interaction_details)
