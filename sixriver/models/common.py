from typing import List
from dataclasses import dataclass, field


@dataclass
class Identifier:

    label: str
    allowed_values: List[str]


@dataclass
class Product:

    id: str
    name: str = None
    description: str = None
    image: str = None
    unit_of_measure: str = None
    unit_of_measure_quantity: int = None
    dimension_unit_of_measure: str = None
    weight_unit_of_measure: str = None
    length: float = None
    width: float = None
    height: float = None
    weight: float = None
    identifiers: List[Identifier] = None


