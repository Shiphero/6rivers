from datetime import datetime

from .pick import GroupType, Pick
from .induct import Induct


class Container(object):

    def __init__(self, id, type=None):
        self.id = id
        self.type = type


class ContainerInducted(object):

    def __init__(
        self,
        timestamp,  # datetime
        group_type,  # GroupType
        group_id,  # str
        container,  # Container
        induct,  # Induct
        picks,  # List['Pick']  # avoid circular dependencies
        data=None,  # dict
    ):
        self.group_type = GroupType(self.group_type)
        self.group_id = group_id
        self.timestamp = timestamp
        self.container = container
        self.induct = induct
        self.picks = picks
        self.data = data or {}


class ContainerPickComplete(object):


    def __init__(
        self,
        timestamp,  # datetime
        group_type,  # GroupType
        group_id,  # str
        container,  # Container
        induct,  # Induct
        picks,  # List['PickComplete']  # avoid circular dependencies
        data=None,  # dict
    ):
        self.timestamp = timestamp
        self.group_id = group_id
        self.group_type = GroupType(self.group_type)
        self.container = container
        self.induct = induct
        self.picks = picks
        self.data = data

    @property
    def has_errors(self):
        return any(pc.failed for pc in self.picks)

    @property
    def short_picks(self):
        return [p for p in self.picks if p.failed]
