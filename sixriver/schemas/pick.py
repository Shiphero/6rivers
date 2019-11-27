from marshmallow import Schema, fields, validates, ValidationError, post_dump, post_load

from sixriver import models

from .common import SixRiverSchema, ProductSchema
from .deserializer import register_schema


@register_schema
class PickSchema(SixRiverSchema):

    __schema_name__ = "pick"

    group_type = fields.Str()
    group_id = fields.Str(data_key='groupID', dump_to="groupID", load_from="groupID")
    pick_id = fields.Str(data_key='pickID', dump_to="pickID", load_from="pickID")
    container = fields.Nested('ContainerSchema')
    packout_container = fields.Nested('ContainerSchema', load_from="packoutContainer")
    source_location = fields.Str(required=True, load_from="sourceLocation")
    destination_location = fields.Str(load_from="destinationLocation")
    each_quantity = fields.Int(required=True, load_from="eachQuantity")
    product = fields.Nested(ProductSchema, required=True)
    expected_shipping_date = fields.DateTime(load_from="expectedShippingDate")
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

    message_type = fields.Str(default=__schema_name__, load_from="messageType")
    started_at = fields.DateTime(load_from="startedAt")
    completed_at = fields.DateTime(load_from="completedAt")
    pick_id = fields.Str(load_from="pickID", dump_to="pickID")
    each_quantity = fields.Int(load_from="eachQuantity")
    source_location = fields.Str(load_from="sourceLocation")
    product = fields.Nested('ProductSchema')
    picked_quantity = fields.Int(load_from="pickedQuantity")
    reason = fields.List(fields.Str())
    captured_identifiers = fields.List(fields.Dict(), many=True, load_from="capturedIdentifiers")
    user_id = fields.Str(load_from="userID", dump_to="userID")
    device_id = fields.Str(load_from="deviceID", dump_to="deviceID")
    data = fields.Dict()

    @post_load
    def make_pick_complete(self, data, **kwargs):
        data.pop('message_type', None)
        return models.PickComplete(**data)


@register_schema
class PickTaskPickedSchema:

    __schema_name__ = "pickTaskPicked"

    message_type = fields.Str(default=__schema_name__, load_from="messageType")
    timestamp = fields.DateTime(required=True)
    pick_id = fields.Str(required=True, load_from="pickID", dump_to="pickID")
    group_id = fields.Str(required=True, load_from="groupID", dump_to="groupID")
    group_type = fields.Str(required=True, load_from="groupType")
    container = fields.Nested('ContainerSchema', required=True)
    induct = fields.Nested('InductSchema', required=True)
    picks = fields.Nested(PickCompleteSchema, many=True)
    user_id = fields.Str(load_from="userID", dump_to="userID")
    device_id = fields.Str(load_from="deviceID", dump_to="deviceID")
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

    message_type = fields.Str(default=__schema_name__, dump_only=True, load_from="messageType")
    picks = fields.Nested(PickSchema, many=True)
