from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Induct:

    started_at: datetime
    completed_at: datetime
    user_id: str
    device_id: str
