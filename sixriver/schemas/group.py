from marshmallow import Schema, fields, validates, ValidationError, post_dump, post_load

from sixriver import models

from .common import SixRiverSchema
from .deserializer import register_schema


@register_schema
class GroupCancelSchema(SixRiverSchema):

    __schema_name__ = "groupCancel"

    message_type = fields.Str(default=__schema_name__, load_from="messageType")
    timestamp = fields.DateTime(required=True)
    group_id = fields.Str(data_key='groupID', dump_to="groupID", load_from="groupID")
    group_type = fields.Str(load_from="groupType")
    container_id = fields.Str(data_key='containerID', dump_to="containerID", load_from="containerID")
    data = fields.Dict()

    @validates('group_type')
    def validate_group_type(self, data, **kwargs):
        valid_types = [models.GroupType.ORDER_PICK.value, models.GroupType.BATCH_PICK.value]
        if data not in valid_types:
            raise ValidationError("Invalid group_type '{}', must be one of {}".format(
                data, valid_types)
            )

    @post_load
    def make_group_cancel(self, data, **kwargs):
        return models.GroupCancel(**data)
