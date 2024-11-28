from kafka import KafkaConsumer
import json
import argparse
from datetime import datetime


class MovementDataConsumer:
    def __init__(self, bootstrap_servers=['localhost:9092'], topic='device-movements'):
        """Initialize the Kafka consumer"""
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=True
        )

    def start_consuming(self, pretty_print=True):
        """Start consuming movement records"""
        try:
            print("Starting to consume movement records...")
            print("Press Ctrl+C to stop")

            for message in self.consumer:
                movement = message.value

                if pretty_print:
                    self._pretty_print_movement(movement)
                else:
                    print(json.dumps(movement))

        except KeyboardInterrupt:
            print("\nStopping movement data consumption...")
        finally:
            self.consumer.close()
            print("Consumer closed.")

    def _pretty_print_movement(self, movement):
        """Print movement record in a readable format"""
        print("\n" + "=" * 50)
        print(f"Timestamp: {movement['timestamp']}")
        print(f"Device ID: {movement['device_id']}")
        print(f"Owner ID: {movement['owner_id']}")
        print(f"Location: {movement['location']['location_id']}")
        print(f"Movement Type: {movement['movement_type']}")
        print(f"Confidence: {movement['confidence_level']}")
        print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description='Consume device movement data from Kafka')
    parser.add_argument(
        '--bootstrap-servers',
        type=str,
        default='localhost:9092',
        help='Kafka bootstrap servers (default: localhost:9092)'
    )
    parser.add_argument(
        '--topic',
        type=str,
        default='device-movements',
        help='Kafka topic name (default: device-movements)'
    )
    parser.add_argument(
        '--raw',
        action='store_true',
        help='Print raw JSON instead of formatted output'
    )

    args = parser.parse_args()

    consumer = MovementDataConsumer(
        bootstrap_servers=args.bootstrap_servers.split(','),
        topic=args.topic
    )

    consumer.start_consuming(pretty_print=not args.raw)


if __name__ == "__main__":
    main()