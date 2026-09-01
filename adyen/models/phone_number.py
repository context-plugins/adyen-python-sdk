from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneNumber(SdkBaseModel):
    number: str
    """The full phone number, including the country code. For example, **+3112345678**."""

    phone_country_code: Optional[str] = Field(default=UNSET, alias="phoneCountryCode")
    """The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code prefix of
    the phone number. For example, **US** or **NL**.

    The value of the ``phoneCountryCode`` is determined by the country code digit(s) of ``phone.number``"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of phone number.
     Possible values: **mobile**, **landline**, **sip**, **fax.**"""


class PhoneNumberDict(TypedDict):
    number: str
    phone_country_code: NotRequired[str]
    type_: NotRequired[str]
