from app.db.new4j_repository.init_data import *
from app.db.model import Location, Device, Interacts
from datetime import datetime


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


def normalization_to_new4j_one_session(data):
    for interaction_data in data:
        devices_data = interaction_data["devices"]
        interaction_details = interaction_data["interaction"]

        device_1_data = devices_data[0]
        device_2_data = devices_data[1]

        location_1 = Location(
            latitude=device_1_data["location"]["latitude"],
            longitude=device_1_data["location"]["longitude"],
            altitude_meters=device_1_data["location"]["altitude_meters"],
            accuracy_meters=device_1_data["location"]["accuracy_meters"],
        )

        location_2 = Location(
            latitude=device_2_data["location"]["latitude"],
            longitude=device_2_data["location"]["longitude"],
            altitude_meters=device_2_data["location"]["altitude_meters"],
            accuracy_meters=device_2_data["location"]["accuracy_meters"],
        )

        device_1 = Device(
            id=device_1_data["id"],
            brand=device_1_data["brand"],
            model=device_1_data["model"],
            os=device_1_data["os"],
        )

        device_2 = Device(
            id=device_2_data["id"],
            brand=device_2_data["brand"],
            model=device_2_data["model"],
            os=device_2_data["os"],
        )

        interaction = Interacts(
            from_device=interaction_details["from_device"],
            to_device=interaction_details["to_device"],
            method=interaction_details["method"],
            bluetooth_version=interaction_details["bluetooth_version"],
            signal_strength_dbm=interaction_details["signal_strength_dbm"],
            distance_meters=interaction_details["distance_meters"],
            duration_seconds=interaction_details["duration_seconds"],
            timestamp=datetime.fromisoformat(interaction_details["timestamp"]),
        )

        process_devices_and_interaction(device_1, device_2, interaction, location_1, location_2)
