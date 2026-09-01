from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountVerificationCountry(str, Enum):
    SE = "SE"
    FI = "FI"
    NO = "NO"
    DK = "DK"
    NL = "NL"
    IT = "IT"
    DE = "DE"
    AT = "AT"
    ES = "ES"
    PT = "PT"
    FR = "FR"
    GB = "GB"
    BE = "BE"
    LV = "LV"
    LT = "LT"
    PL = "PL"
    EE = "EE"
    IE = "IE"
    US = "US"
    CA = "CA"
    AU = "AU"

    __str__ = str.__str__


AccountVerificationCountryOrStr: TypeAlias = Annotated[
    AccountVerificationCountry | str, open_enum_validator(AccountVerificationCountry)
]
