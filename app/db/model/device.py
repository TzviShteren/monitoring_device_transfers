from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime


@dataclass
class Device:
    id: str
    brand: str
    model: str
    os: str
