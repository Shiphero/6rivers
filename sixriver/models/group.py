import enum

#from dataclasses import dataclass

from .pick import GroupType, convert_group_type


#@dataclass
class GroupCancel(object):

    def __init__(
        self,
        timestamp,  # datetime
        group_id,  # str
        group_type,  # GroupType = GroupType.ORDER_PICK
        container_id=None,  # str = None
        data=None,  # str = None
    ):
        self.timestamp = timestamp
        self.group_id = group_id
        self.group_type = convert_group_type(group_type)
        self.container_id = container_id
        self.data = data

