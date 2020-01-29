from datetime import date
from marshmallow import Schema, fields, pprint, post_dump, post_load, pre_load

from .. import models

from .common import SixRiverSchema




class InductSchema(SixRiverSchema):

    __schema_name__ = "induct"

    started_at = fields.DateTime(load_from="startedAt")
    completed_at = fields.DateTime(load_from="completedAt")
    user_id = fields.Str(data_key='userID', load_from="userID", required=True)
    device_id = fields.Str(data_key='deviceID', load_from="deviceID", required=True)

    @pre_load
    def remove_empty(self, item, **kwargs):
        for f in ("startedAt", "completedAt"):
            if not item.get(f):
                item.pop(f, None)

        return item

    @post_load
    def make_induct(self, data, **kwargs):
        return models.Induct(**data)
