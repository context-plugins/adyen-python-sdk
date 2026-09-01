from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeWindowSize(str, Enum):
    """Dimensions of the 3DS2 challenge window to be displayed to the cardholder.

    Possible values:

    * **01** - size of 250x400
    * **02** - size of 390x400
    * **03** - size of 500x600
    * **04** - size of 600x400
    * **05** - Fullscreen"""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"

    __str__ = str.__str__


ChallengeWindowSizeOrStr: TypeAlias = Annotated[ChallengeWindowSize | str, open_enum_validator(ChallengeWindowSize)]
