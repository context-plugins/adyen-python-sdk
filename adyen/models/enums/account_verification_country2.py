from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountVerificationCountry2(str, Enum):
    """The location where the third-party individual's bank account is registered. Adyen uses this information to
    determine an available open banking provider, and to configure the open banking flow for that respective
    location."""

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


AccountVerificationCountry2OrStr: TypeAlias = Annotated[
    AccountVerificationCountry2 | str, open_enum_validator(AccountVerificationCountry2)
]
