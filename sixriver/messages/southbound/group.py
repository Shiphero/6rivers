import requests

from datetime import datetime
from marshmallow import fields, validates, ValidationError

from .base import SouthboundMessage
from sixriver.models import GroupType


class GroupCancelMessage(SouthboundMessage):

    __endpoint__ = 'group-cancellations'
    __http_method__ = requests.post

    def __init__(self, group_id, group_type=None, container_id=None):
        self._group_id = group_id
        self._group_type = group_type or GroupType.ORDER_PICK
        self._container_id = container_id
        self._timestamp = datetime.utcnow()

    def serialize(self):
        from sixriver import schemas

        return schemas.GroupCancelSchema().dump(dict(
            group_id=self._group_id,
            group_type=self._group_type,
            container_id=self._container_id,
            timestamp=self._timestamp,
        ))

