from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TrackFormat1(str, Enum):
    """Card track format. Possible values:
    * **AAMVA**
    * **ISO**"""

    ISO = "ISO"
    JIS_I = "JIS-I"
    JIS_II = "JIS-II"
    AAMVA = "AAMVA"
    CMC_7 = "CMC-7"
    E_13_B = "E-13B"

    __str__ = str.__str__


TrackFormat1OrStr: TypeAlias = Annotated[TrackFormat1 | str, open_enum_validator(TrackFormat1)]
