from typing import List
from dataclasses import dataclass, field

from datetime import datetime

from .pick import GroupType, Pick
from .induct import Induct


@dataclass
class Container:

    id: str
    type: str


@dataclass
class ContainerInducted:

    timestamp: datetime
    group_type: GroupType
    group_id: str
    container: Container
    induct: Induct
    picks: List['Pick']  # avoid circular dependencies
    data: dict

    def __post_init__(self):
        self.group_type = GroupType(self.group_type)


@dataclass
class ContainerPickComplete:

    timestamp: datetime
    group_type: GroupType
    group_id: str
    container: Container
    induct: Induct
    picks: List['PickComplete']  # avoid circular dependencies
    user_id: str = None
    device_id: str = None
    data: dict

    @property
    def has_errors(self):
        return any(pc.failed for pc in self.picks)

    @property
    def short_picks(self):
        return [p for p in self.picks if p.failed]
