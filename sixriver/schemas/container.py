from datetime import date
from marshmallow import Schema, fields, pprint, post_load

from .. import models

from .common import SixRiverSchema
from .deserializer import register_schema


@register_schema
class ContainerSchema(SixRiverSchema):

    __schema_name__ = "container"

    id = fields.Str(data_key="containerID", load_from="containerID", dump_to="containerID")
    container_type = fields.Raw(loadFrom="containerType")  # this can be a str or a list of str

    @post_load
    def make_container(self, data, **kwargs):
        return models.Container(**data)


@register_schema
class ContainerInductedSchema(SixRiverSchema):

    __schema_name__ = "containerInducted"

    message_type = fields.Str(default=__schema_name__, required=True, load_from="messageType")
    timestamp = fields.AwareDateTime()
    group_type = fields.Str(load_from="groupType")
    group_id = fields.Str(data_key="groupID", load_from="groupID", dump_to="groupID")
    container = fields.Nested(ContainerSchema)
    induct = fields.Nested('InductSchema')
    picks = fields.Nested('PickSchema', many=True)
    data = fields.Dict()

    @post_load
    def make_container_inducted(self, data, **kwargs):
        data.pop('message_type', None)
        return models.ContainerInducted(**data)


@register_schema
class ContainerPickCompleteSchema(SixRiverSchema):

    __schema_name__ = "containerPickComplete"

    message_type = fields.Str(default=__schema_name__, required=True, load_from="messageType")
    timestamp = fields.AwareDateTime()
    group_type = fields.Str(load_from="groupType")
    group_id = fields.Str(data_key="groupID", load_from="groupID", dump_to="groupID")
    container = fields.Nested(ContainerSchema)
    induct = fields.Nested('InductSchema')
    picks = fields.Nested('PickCompleteSchema', many=True)
    user_id = fields.Str(data_key="userID", load_from="userID", dump_to="userID")
    device_id = fields.Str(data_key="deviceID", load_from="deviceID", dump_to="deviceID")
    data = fields.Dict()

    @post_load
    def make_container_pick_complete(self, data, **kwargs):
        data.pop('message_type', None)
        return models.ContainerPickComplete(**data)
