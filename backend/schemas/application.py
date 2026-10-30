from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

class ApplicationStatus(str, Enum):
    DISCOVERED = "discovered"
    INTERESTED = "interested"
    APPLIED = "applied"
    ON_HOLD = "on_hold"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    EXPIRED = "expired"
    OFFER = "offer"
