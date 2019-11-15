import enum

from datetime import date
from marshmallow import Schema, fields, pprint, post_dump, post_load

try:
    from marshmallow import EXCLUDE
except:
    EXCLUDE = "exclude"

from sixriver.utils import camelcase
from sixriver import models

from .deserializer import register_schema


class SixRiverSchema(Schema):
    """
    Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    __schema_name__ = None

    class Meta:
        unknown = EXCLUDE

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)

    @post_dump(pass_many=True, pass_original=True)
    def normalize(self, data, original_data, many, **kwargs):
        original_data = original_data if many else [original_data]
        _data = data if many else [data]

        # Inspect the original object to convert enums
        for idx, e in enumerate(original_data):
            obj = e if isinstance(e, dict) else e.__dict__
            for key, value in obj.items():
                if isinstance(value, enum.Enum):
                    _data[idx][camelcase(key)] = value.value

        # Let's remove None fields from the serialization
        for e in _data:
            for key, value in dict(e).items():
                if value is None:
                    e.pop(key)

        return data


@register_schema
class IdentifierSchema(SixRiverSchema):

    __schema_name__ = "identifier"

    label = fields.Str(required=True)
    allowed_values = fields.Nested(fields.Str, many=True)

    @post_load
    def make_identifier(self, data, **kwargs):
        return models.Identifier(**data)


@register_schema
class ProductSchema(SixRiverSchema):

    __schema_name__ = "product"

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

    @post_load
    def make_product(self, data, **kwargs):
        return models.Product(**data)
