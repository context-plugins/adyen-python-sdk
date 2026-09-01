from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType11(str, Enum):
    """The type of product that you purchased.

    Possible values: **goods**, **services**."""

    GOODS = "goods"
    SERVICES = "services"

    __str__ = str.__str__


ProductType11OrStr: TypeAlias = Annotated[ProductType11 | str, open_enum_validator(ProductType11)]
