from marshmallow import Schema, fields, validates, ValidationError, post_dump

from SixRiver import models
from .common import SixRiverSchema, ContainerSchema, ProductSchema


class PickSchema(SixRiverSchema):

    group_type = fields.Str()
    group_id = fields.Str(data_key='groupID')
    pick_id = fields.Str(data_key='pickID')
    container = fields.Nested(ContainerSchema)
    packout_container = fields.Nested(ContainerSchema)
    source_location = fields.Str(required=True)
    destination_location = fields.Str()
    each_quantity = fields.Int(required=True)
    product = fields.Nested(ProductSchema, required=True)
    expected_shipping_date = fields.DateTime()
    data = fields.Dict()

    @validates('group_type')
    def validate_group_type(self, data, **kwargs):
        valid_types = [models.GroupType.ORDER_PICK.value, models.GroupType.BATCH_PICK.value]
        if data not in valid_types:
            raise ValidationError(f'Invalid group_type, must be one of {valid_types}')

