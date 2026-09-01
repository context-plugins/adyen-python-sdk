from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value6(str, Enum):
    CARD = "CARD"
    MOBILE_PHONE = "MOBILE_PHONE"
    OTHER = "OTHER"
    PC = "PC"
    TABLET_OR_EREADER = "TABLET_OR_EREADER"
    UNKNOWN = "UNKNOWN"
    WATCH_OR_WRISTBAND = "WATCH_OR_WRISTBAND"
    WEARABLE = "WEARABLE"

    __str__ = str.__str__


Value6OrStr: TypeAlias = Annotated[Value6 | str, open_enum_validator(Value6)]
