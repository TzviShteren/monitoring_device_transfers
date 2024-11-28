from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Location:
    latitude: float
    longitude: float
    altitude_meters: int
    accuracy_meters: int

