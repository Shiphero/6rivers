import enum

from datetime import date
from marshmallow import Schema, fields, pprint, post_dump

from SixRiver.utils import camelcase


class SixRiverSchema(Schema):
    """
    Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)

    @post_dump(pass_many=True, pass_original=True)
    def convert_enums(self, data, original_data, many, **kwargs):
        original_data = original_data if many else [original_data]
        _data = data if many else [data]

        for idx, e in enumerate(original_data):
            obj = e if isinstance(e, dict) else e.__dict__
            for key, value in obj.items():
                if isinstance(value, enum.Enum):
                    _data[idx][camelcase(key)] = value.value

        return data

class ContainerSchema(SixRiverSchema):

    id = fields.Str()
    type = fields.Str()


class IdentifierSchema(SixRiverSchema):

    label = fields.Str(required=True)
    allowed_values = fields.Nested(fields.Str, many=True)


class ProductSchema(SixRiverSchema):

    id = fields.Str(required=True, data_key='productID')
    name = fields.Str()
    description = fields.Str()
    image = fields.Url()
    unit_of_measure = fields.Str()
    unit_of_measure_quantity = fields.Int()
    dimension_unit_of_measure = fields.Str()
    length = fields.Float()
    width = fields.Float()
    height = fields.Float()
    weight = fields.Float()
    identifiers = fields.Nested(IdentifierSchema, many=True)
