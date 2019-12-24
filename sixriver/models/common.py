from typing import List
# from dataclasses import dataclass, field


# @dataclass
# class Identifier:

#     label: str
#     allowed_values: List[str]


# @dataclass
# class Product:

#     id: str
#     name: str=None
#     description: str=None
#     image: str=None
#     unit_of_measure: str=None
#     unit_of_measure_quantity: int=None
#     dimension_unit_of_measure: str=None
#     weight_unit_of_measure: str=None
#     length: float=None
#     width: float=None
#     height: float=None
#     weight: float=None
#     identifiers: List[Identifier]=None


class Identifier(object):

    def __init__(
        self,
        label,  # str
        allowed_values  # List[str]
    ):
        self.label = label
        self.allowed_values = allowed_values


class Product(object):

    def __init__(
        self,
        id,  # str
        name=None,  # str=None
        description=None,  # str=None
        image=None,  # str=None
        unit_of_measure=None,  # str=None
        unit_of_measure_quantity=None,  # int=None
        dimension_unit_of_measure=None,  # str=None
        weight_unit_of_measure=None,  # str=None
        length=None,  # float=None
        width=None,  # float=None
        height=None,  # float=None
        weight=None,  # float=None
        identifiers=None,  # List[Identifier]=None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.unit_of_measure = unit_of_measure
        self.unit_of_measure_quantity = unit_of_measure_quantity
        self.dimension_unit_of_measure = dimension_unit_of_measure
        self.weight_unit_of_measure = weight_unit_of_measure
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.identifiers = identifiers


