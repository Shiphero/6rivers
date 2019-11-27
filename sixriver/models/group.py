import enum

from dataclasses import dataclass

from .pick import GroupType, convert_group_type


@dataclass
class GroupCancel(object):

    timestamp: datetime
    group_id: str
    group_type: GroupType = GroupType.ORDER_PICK
    container_id: str = None
    data: str = None

    def __post_init__(self):
        self.group_type = convert_group_type(self.group_type)
