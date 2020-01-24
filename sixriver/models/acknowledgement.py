
from datetime import datetime


class AcknowledgementError(object):

    def __init__(
        self,
        code: str,
        data: dict = None,
    ):
        self.code = code
        self.data = data


class Acknowledgement(object):

    def __init__(
        self,
        timestamp: datetime,
        group_id: str,
        request_type: str,
        error: AcknowledgementError = None,
        data: dict = None,
    ):
        self.timestamp = timestamp
        self.group_id = group_id
        self.request_type = request_type
        self.error = error
        self.data = data

    @property
    def is_group_cancel(self):
        return self.request_type == "groupCancel"

    @property
    def is_failure(self):
        return self.error is not None
