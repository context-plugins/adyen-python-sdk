from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PanEntryMode(str, Enum):
    """Indicates the method used for entering the PAN to initiate a transaction.

    Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**."""

    CHIP = "chip"
    COF = "cof"
    CONTACTLESS = "contactless"
    ECOMMERCE = "ecommerce"
    MAGSTRIPE = "magstripe"
    MANUAL = "manual"
    TOKEN = "token"

    __str__ = str.__str__


PanEntryModeOrStr: TypeAlias = Annotated[PanEntryMode | str, open_enum_validator(PanEntryMode)]
