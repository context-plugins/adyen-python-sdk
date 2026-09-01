from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TrackFormat(str, Enum):
    """Magnetic track or magnetic ink characters line. Possible values:
    * **ISO**
    * **JIS-I**
    * **JIS-II**
    * **AAMVA**
    * **CMC-7**
    * **E-13B**"""

    ISO = "ISO"
    JIS_I = "JIS-I"
    JIS_II = "JIS-II"
    AAMVA = "AAMVA"
    CMC_7 = "CMC-7"
    E_13_B = "E-13B"

    __str__ = str.__str__


TrackFormatOrStr: TypeAlias = Annotated[TrackFormat | str, open_enum_validator(TrackFormat)]
