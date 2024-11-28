from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Device:
    owner_name: str
    type: str
    status: bool
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    device_id: Optional[uuid] = None
