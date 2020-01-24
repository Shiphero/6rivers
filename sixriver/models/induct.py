#from dataclasses import dataclass, field
from datetime import datetime


#@dataclass
class Induct(object):

    def __init__(
        self,
        user_id,  # str
        device_id,  # str
        started_at=None,  # datetime
        completed_at=None,  # datetime
    ):
        self.started_at = started_at
        self.completed_at = completed_at
        self.user_id = user_id
        self.device_id = device_id
