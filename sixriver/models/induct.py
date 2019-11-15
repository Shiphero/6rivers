from datetime import datetime


class Induct(object):

    def __init__(
        self,
        started_at,  # datetime
        completed_at,  # datetime
        user_id,  # :str
        device_id,  # str
    ):
        self.started_at = started_at
        self.completed_at = completed_at
        self.user_id = user_id
        self.device_id = device_id
