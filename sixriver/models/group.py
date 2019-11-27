import enum


class GroupCancel(object):

    def __init__(
        self,
        timestamp,  # datetime
        group_id,  # str
        group_type,  # GroupType
        container_id=None,  # str
        data=None,  # str = None
    ):
        self.group_type = convert_group_type(group_type)
        self.timestamp = timestamp
        self.container_id = container_id
        self.group_id = group_id
        self.data = data or {}
