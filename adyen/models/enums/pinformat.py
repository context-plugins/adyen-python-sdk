from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Pinformat(str, Enum):
    ISO0 = "ISO0"
    ISO1 = "ISO1"
    ISO2 = "ISO2"
    ISO3 = "ISO3"

    __str__ = str.__str__


PinformatOrStr: TypeAlias = Annotated[Pinformat | str, open_enum_validator(Pinformat)]
