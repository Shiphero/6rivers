import enum

from datetime import datetime
from typing import List, Type
from dataclasses import dataclass, field

from .common import Identifier, Product
from ..utils import camelcase


class GroupType(enum.Enum):

    ORDER_PICK = 'orderPick'
    BATCH_PICK = 'batchPick'


def convert_group_type(group_type):
    valid_group_types = [GroupType.ORDER_PICK, GroupType.BATCH_PICK]
    val = group_type

    if isinstance(val, str):
        val = GroupType(val)

    elif val not in valid_group_types:
        raise ValueError(f"Invalid group type, must be one of {valid_group_types}")

    return val


@dataclass
class Pick(object):

    source_location: str
    each_quantity: int
    product: Product

    group_type: GroupType = GroupType.ORDER_PICK
    group_id: str = None
    pick_id: str = None
    container: List['Container'] = None
    packout_container: List['Container'] = None
    destination_location: str = None
    expected_shipping_date: datetime = None
    data: dict = None

    def __post_init__(self):
        self.group_type = convert_group_type(self.group_type)


@dataclass
class PickComplete:

    started_at: datetime
    completed_at: datetime
    pick_id: str
    each_quantity: int
    source_location: str
    product: Product
    picked_quantity: int
    reason: List[str] = None
    captured_identifiers: List[dict] = None
    user_id: str = None
    device_id: str = None
    data: dict = None

    @property
    def is_shortpick(self):
        return self.each_quantity != self.picked_quantity

    @property
    def failed(self):
        return self.reason not in [None, []]


@dataclass
class PickTaskPicked:

    timestamp: datetime
    pick_id: str
    group_id: str
    group_type: GroupType
    container: Type['Container']
    induct: Type['Induct']
    picks: List[PickComplete]
    user_id: str = None
    device_id: str = None
    data: str = None

    def __post_init__(self):
        self.group_type = convert_group_type(self.group_type)

    @property
    def has_errors(self):
        return any(pc.failed for pc in self.picks)

    @property
    def short_picks(self):
        return [p for p in self.picks if p.failed]
