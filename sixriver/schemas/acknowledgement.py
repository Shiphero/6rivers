from marshmallow import Schema, fields, validates, ValidationError, post_dump, post_load

from sixriver import models

from .common import SixRiverSchema



class AcknowledgementErrorSchema(SixRiverSchema):

    code = fields.Str()
    data = fields.Dict()

    @post_load
    def make_container_inducted(self, data, **kwargs):
        return models.AcknowledgementError(**data)



class AcknowledgementSchema(SixRiverSchema):

    __schema_name__ = "acknowledgement"

    message_type = fields.Str(default=__schema_name__, load_from="messageType")
    timestamp = fields.DateTime(required=True)
    group_id = fields.Str(data_key='groupID', dump_to="groupID", load_from="groupID")
    request_type = fields.Str(data_key='requestType', load_from="requestType")
    error = fields.Nested("AcknowledgementErrorSchema")
    data = fields.Dict()

    @post_load
    def make_container_inducted(self, data, **kwargs):
        data.pop('message_type', None)
        return models.Acknowledgement(**data)
