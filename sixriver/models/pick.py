import enum

from datetime import datetime
from typing import List
from dataclasses import dataclass, field

from SixRiver.utils import camelcase

from .common import Identifier, Container, Product


class GroupType(enum.Enum):

    ORDER_PICK = 'orderPick'
    BATCH_PICK = 'batchPick'


@dataclass
class Pick(object):

    source_location: str
    each_quantity: int
    product: Product

    group_type: GroupType = GroupType.ORDER_PICK
    group_id: str = None
    pick_id: str = None
    container: List[Container] = None
    packout_container: List[Container] = None
    destination_location: str = None
    expected_shipping_date: datetime = None
    data: dict = None


    def __post_init__(self):
        valid_group_types = [GroupType.ORDER_PICK, GroupType.BATCH_PICK]
        if self.group_type not in valid_group_types:
            raise ValueError(f"Invalid group type, must be one of {valid_group_types}")

