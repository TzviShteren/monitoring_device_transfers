from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Location:
    type: str
    risk_level: int
    name: Optional[str] = None
    location_id: Optional[uuid.UUID] = None

