from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType21(str, Enum):
    """The type of product that you expected to receive.

    Possible values: **goods**, **services**."""

    GOODS = "goods"
    SERVICES = "services"

    __str__ = str.__str__


ProductType21OrStr: TypeAlias = Annotated[ProductType21 | str, open_enum_validator(ProductType21)]
