from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentificationType1(str, Enum):
    """Possible values:
    * **PAN**
    * **ISOTrack2**
    * **BarCode**
    * **AccountNumber**
    * **PhoneNumber**"""

    PAN = "PAN"
    ISO_TRACK2 = "ISOTrack2"
    BAR_CODE = "BarCode"
    ACCOUNT_NUMBER = "AccountNumber"
    PHONE_NUMBER = "PhoneNumber"

    __str__ = str.__str__


IdentificationType1OrStr: TypeAlias = Annotated[IdentificationType1 | str, open_enum_validator(IdentificationType1)]
