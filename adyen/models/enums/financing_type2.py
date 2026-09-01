from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FinancingType2(str, Enum):
    """The type of financing that the offer is for.

    Possible values: **businessFinancing**."""

    HARDWARE_FINANCING = "hardwareFinancing"
    BUSINESS_FINANCING = "businessFinancing"

    __str__ = str.__str__


FinancingType2OrStr: TypeAlias = Annotated[FinancingType2 | str, open_enum_validator(FinancingType2)]
