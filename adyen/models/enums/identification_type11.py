from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentificationType11(str, Enum):
    """Type of account identification. In a request message, it informs the POI System the type of the account or card
    identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the
    Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card
    identification. Possible values:
    * **AccountNumber**
    * **BarCode**
    * **ISOTrack2**
    * **PAN**
    * **PhoneNumber**"""

    PAN = "PAN"
    ISO_TRACK2 = "ISOTrack2"
    BAR_CODE = "BarCode"
    ACCOUNT_NUMBER = "AccountNumber"
    PHONE_NUMBER = "PhoneNumber"

    __str__ = str.__str__


IdentificationType11OrStr: TypeAlias = Annotated[IdentificationType11 | str, open_enum_validator(IdentificationType11)]
