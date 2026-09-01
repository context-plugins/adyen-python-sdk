from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType(str, Enum):
    ONBOARDING = "onboarding"
    PLATFORM = "platform"
    BANK = "bank"

    __str__ = str.__str__


ProductTypeOrStr: TypeAlias = Annotated[ProductType | str, open_enum_validator(ProductType)]
