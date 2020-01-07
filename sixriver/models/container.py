from typing import List
#from dataclasses import dataclass, field

from datetime import datetime

from .pick import GroupType, Pick
from .induct import Induct


#@dataclass
class Container(object):

    def __init__(
        self,
        id=None,  # str = None
        container_type=None,  # str = None
    ):
        self.id = id
        self.container_type = container_type

#@dataclass
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
        self.group_type = GroupType(group_type)
        self.timestamp = timestamp
        self.group_id = group_id
        self.container = container
        self.induct = induct
        self.picks = picks
        self.data = data


#@dataclass
class ContainerPickComplete(object):

    def __init__(
        self,
        timestamp,  # datetime
        group_type,  # GroupType
        group_id,  # str
        container,  # Container
        picks,  # List['PickComplete']  # avoid circular dependencies
        induct=None,  # Induct
        user_id=None,  # str = None
        device_id=None,  # str = None
        data=None,  # dict
    ):
        self.timestamp = timestamp
        self.group_type = GroupType(group_type)
        self.group_id = group_id
        self.container = container
        self.induct = induct
        self.picks = picks
        self.user_id = user_id
        self.device_id = device_id
        self.data = data

    @property
    def has_errors(self):
        return any(pc.failed for pc in self.picks)

    @property
    def short_picks(self):
        return [p for p in self.picks if p.failed]
