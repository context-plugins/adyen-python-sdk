from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FinancingType(str, Enum):
    HARDWARE_FINANCING = "hardwareFinancing"
    BUSINESS_FINANCING = "businessFinancing"

    __str__ = str.__str__


FinancingTypeOrStr: TypeAlias = Annotated[FinancingType | str, open_enum_validator(FinancingType)]
