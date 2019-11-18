import enum

from datetime import datetime

from .common import Identifier, Product
from sixriver.utils import camelcase


class GroupType(enum.Enum):

    ORDER_PICK = 'orderPick'
    BATCH_PICK = 'batchPick'


def convert_group_type(group_type):
    valid_group_types = [GroupType.ORDER_PICK, GroupType.BATCH_PICK]
    val = group_type

    if isinstance(val, str):
        val = GroupType(val)

    elif val not in valid_group_types:
        raise ValueError("Invalid group type, must be one of {}".format(valid_group_types))

    return val


class Pick(object):

    def __init__(
        self,
        source_location,  # str
        each_quantity,  # int
        product,  # Product
        group_type=GroupType.ORDER_PICK,  # GroupType = GroupType.ORDER_PICK
        group_id=None,  # str = None
        pick_id=None,  # str = None
        container=None,  # List['Container'] = None
        packout_container=None,  # List['Container'] = None
        destination_location=None,  # str = None
        expected_shipping_date=None,  # datetime = None
        data=None,  # dict = None
    ):
        self.source_location = source_location
        self.each_quantity = each_quantity
        self.product = product
        self.group_type = convert_group_type(group_type)
        self.group_id = group_id
        self.pick_id = pick_id
        self.container = container
        self.packout_container = packout_container
        self.destination_location = destination_location
        self.expected_shipping_date = expected_shipping_date
        self.data = data or {}


class PickComplete(object):

    def __init__(
        self,
        started_at,  # datetime
        completed_at,  # datetime
        pick_id,  # str
        each_quantity,  # int
        source_location,  # str
        product,  # Product
        picked_quantity,  # int
        reason=None,  # List[str] = None
        captured_identifiers=None,  # List[dict] = None
        user_id=None,  # str = None
        device_id=None,  # str = None
        data=None,  # dict = None
    ):
        self.started_at = started_at
        self.completed_at = completed_at
        self.pick_id = pick_id
        self.each_quantity = each_quantity
        self.source_location = source_location
        self.product = product
        self.picked_quantity = picked_quantity
        self.reason = reason
        self.captured_identifiers = captured_identifiers
        self.user_id = user_id
        self.device_id = device_id
        self.data = data or {}

    @property
    def failed(self):
        return self.reason not in [None, []]


class PickTaskPicked(object):

    def __init__(
        self,
        timestamp,  # datetime
        pick_id,  # str
        group_id,  # str
        group_type,  # GroupType
        container,  # Type['Container']
        induct,  # Type['Induct']
        picks,  # List[PickComplete]
        user_id=None,  # str = None
        device_id=None,  # str = None
        data=None,  # str = None
    ):
        self.group_type = convert_group_type(group_type)
        self.timestamp = timestamp
        self.pick_id = pick_id
        self.group_id = group_id
        self.container = container
        self.induct = induct
        self.picks = picks
        self.user_id = user_id
        self.device_id = device_id
        self.data = data or {}

    @property
    def has_errors(self):
        return any(pc.failed for pc in self.picks)

    @property
    def short_picks(self):
        return [p for p in self.picks if p.failed]
