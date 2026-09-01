from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType1(str, Enum):
    GOODS = "goods"
    SERVICES = "services"

    __str__ = str.__str__


ProductType1OrStr: TypeAlias = Annotated[ProductType1 | str, open_enum_validator(ProductType1)]
