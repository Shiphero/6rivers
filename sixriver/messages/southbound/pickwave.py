import requests

from marshmallow import fields, validates, ValidationError

from .base import SouthboundMessage


class PickWaveMessage(SouthboundMessage):

    __endpoint__ = 'pick-wave'
    __http_method__ = requests.post

    def __init__(self, *picks):
        self._picks = picks or []

    def add_picks(self, *picks):
        self._picks.extend(picks)

    def serialize(self):
        from sixriver import schemas

        return schemas.PickWaveSchema().dump(dict(
            picks=self._picks
        ))

