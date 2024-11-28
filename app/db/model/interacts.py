from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Interacts:
    from_device: str
    to_device: str
    method: str
    bluetooth_version: str
    signal_strength_dbm: int
    distance_meters: float
    duration_seconds: int
    timestamp: datetime
