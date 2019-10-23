from marshmallow import Schema, fields, validates, ValidationError, post_dump, post_load

from sixriver import models

from .common import SixRiverSchema, ProductSchema
from .deserializer import register_schema


@register_schema
class PickSchema(SixRiverSchema):

    __schema_name__ = "pick"

    group_type = fields.Str()
    group_id = fields.Str(data_key='groupID')
    pick_id = fields.Str(data_key='pickID')
    container = fields.Nested('ContainerSchema')
    packout_container = fields.Nested('ContainerSchema')
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

    @post_load
    def make_pick(self, data, **kwargs):
        return models.Pick(**data)


@register_schema
class PickCompleteSchema:

    __schema_name__ = "pickComplete"

    started_at = fields.DateTime()
    completed_at = fields.DateTime()
    pick_id = fields.Str()
    each_quantity = fields.Int()
    source_location = fields.Str()
    product = fields.Nested('ProductSchema')
    picked_quantity = fields.Int()
    reason = fields.List(fields.Str())
    captured_identifiers = fields.Nested(fields.Dict(), many=True)
    user_id = fields.Str()
    device_id = fields.Str()
    data = fields.Dict()

    @post_load
    def make_pick_complete(self, data, **kwargs):
        return models.PickComplete(**data)


@register_schema
class PickTaskPickedSchema:

    __schema_name__ = "pickTaskPicked"

    message_type = fields.Str(default=__schema_name__, required=True)
    timestamp = fields.DateTime(required=True)
    pick_id = fields.Str(required=True)
    group_id = fields.Str(required=True)
    group_type = fields.Str(required=True)
    container = fields.Nested('ContainerSchema', required=True)
    induct = fields.Nested('InductSchema', required=True)
    picks = fields.Nested(PickCompleteSchema, many=True)
    user_id = fields.Str()
    device_id = fields.Str()
    data = fields.Dict()

    @validates('group_type')
    def validate_group_type(self, data, **kwargs):
        valid_types = [models.GroupType.ORDER_PICK.value, models.GroupType.BATCH_PICK.value]
        if data not in valid_types:
            raise ValidationError(f'Invalid group_type, must be one of {valid_types}')

    @post_load
    def make_pick_task_picked(self, data, **kwargs):
        return models.PickTaskPicked(**data)


@register_schema
class PickWaveSchema(SixRiverSchema):

    __schema_name__ = "pickWave"

    message_type = fields.Str(default=__schema_name__, dump_only=True)
    picks = fields.Nested(PickSchema, many=True)
