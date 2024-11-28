from app.db.new4j_repository.init_data import *
from app.db.new4j_repository.device_repository import set_device_location


def normalization_to_new4j(data):
    for interaction in data:
        devices = interaction["devices"]
        interaction_details = interaction["interaction"]
        for device in devices:
            if not device_exist(device["id"]):
                create_device(device)
                print(f"new device {device} created")
        if device_exist(devices[0]["id"]) and device_exist(devices[1]["id"]):
            create_interaction_details(interaction_details)
            print(f"new interaction {interaction_details} created")
