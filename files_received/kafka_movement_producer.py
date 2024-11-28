from kafka import KafkaProducer
import json
import time
from datetime import datetime, timedelta
import random
import sys

# Configuration - Change these values as needed
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'device-movements'
INTERVAL_SECONDS = 60  # Change this to modify frequency (e.g., 60 for 1 minute, 300 for 5 minutes)
MAX_RECORDS = None  # Set a number to limit total records, or None for unlimited


class MovementDataProducer:
    def __init__(self):
        """Initialize the Kafka producer with test data configuration"""
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

        # Test data configuration
        self.device_ids = [f"D{i:05d}" for i in range(50)]
        self.owner_ids = [f"O{i:05d}" for i in range(30)]
        self.location_ids = [f"L{i:05d}" for i in range(20)]
        self.movement_types = ["walking", "vehicle", "stationary"]

        # Simulate some fixed patterns
        self.patterns = self._create_movement_patterns()

    def _create_movement_patterns(self):
        """Create some predefined movement patterns"""
        patterns = []

        # Create circular patterns
        for i in range(5):
            pattern = {
                'device_id': random.choice(self.device_ids),
                'owner_id': random.choice(self.owner_ids),
                'locations': random.sample(self.location_ids, 3)
            }
            patterns.append(pattern)

        return patterns

    def generate_movement(self, use_patterns=True):
        """Generate a single movement record"""
        if use_patterns and random.random() < 0.3:  # 30% chance to use a pattern
            pattern = random.choice(self.patterns)
            location_id = random.choice(pattern['locations'])
            device_id = pattern['device_id']
            owner_id = pattern['owner_id']
        else:
            device_id = random.choice(self.device_ids)
            owner_id = random.choice(self.owner_ids)
            location_id = random.choice(self.location_ids)

        return {
            "device_id": device_id,
            "owner_id": owner_id,
            "timestamp": datetime.now().isoformat(),
            "location": {
                "location_id": location_id
            },
            "movement_type": random.choice(self.movement_types),
            "confidence_level": round(random.uniform(0.7, 1.0), 2)
        }

    def produce_movements(self):
        """Produce movement records at specified intervals"""
        records_produced = 0

        try:
            print(f"Starting to produce movement records every {INTERVAL_SECONDS} seconds...")
            print("Press Ctrl+C to stop")

            while True:
                if MAX_RECORDS and records_produced >= MAX_RECORDS:
                    print(f"\nReached maximum records ({MAX_RECORDS}). Stopping.")
                    break

                # Generate and send movement data
                movement = self.generate_movement()
                self.producer.send(KAFKA_TOPIC, value=movement)

                # Print progress
                records_produced += 1
                print(f"\rRecords produced: {records_produced}", end='')
                sys.stdout.flush()

                # Wait for next interval
                time.sleep(INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print("\nStopping movement data production...")
        finally:
            self.producer.close()
            print("\nProducer closed.")


if __name__ == "__main__":
    producer = MovementDataProducer()
    producer.produce_movements()