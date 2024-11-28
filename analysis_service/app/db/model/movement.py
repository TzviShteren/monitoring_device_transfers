from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Movement:
    timestamp: datetime
    confidence_level: float
    movement_type: str
    duration: Optional[int] = None
