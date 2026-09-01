from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value2(str, Enum):
    BARCODE = "barcode"
    CHIP = "chip"
    COF = "cof"
    CONTACTLESS = "contactless"
    MAGSTRIPE = "magstripe"
    MANUAL = "manual"
    OCR = "ocr"
    SERVER = "server"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Value2OrStr: TypeAlias = Annotated[Value2 | str, open_enum_validator(Value2)]
