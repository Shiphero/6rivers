import requests

from marshmallow import fields, validates, ValidationError

from SixRiver.schemas import SixRiverSchema, PickSchema
from ..base import SixRiverMessage


class PickWaveSchema(SixRiverSchema):

    message_type = fields.Str(default="pickWave", dump_only=True)
    picks = fields.Nested(PickSchema, many=True)


class PickWaveMessage(SixRiverMessage):

    __endpoint__ = 'pick-wave'
    __http_method__ = requests.post

    def __init__(self, *picks):
        self._picks = picks or []

    def add_picks(self, *picks):
        self._picks.extend(picks)

    def serialize(self):
        return PickWaveSchema().dump(dict(
            picks=self._picks
        ))

