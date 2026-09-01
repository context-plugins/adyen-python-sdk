from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.phone_type import PhoneTypeOrStr


class ViasPhoneNumber2(SdkBaseModel):
    """The phone number of the entity."""

    phone_country_code: Optional[str] = Field(default=UNSET, alias="phoneCountryCode")
    """The two-character country code of the phone number. >The permitted country codes are defined in ISO-3166-1
    alpha-2 (e.g. 'NL')."""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The phone number. >The inclusion of the phone number country code is not necessary."""

    phone_type: Optional[PhoneTypeOrStr] = Field(default=UNSET, alias="phoneType")
    """The type of the phone number. >The following values are permitted: ``Landline``, ``Mobile``, ``SIP``, ``Fax``."""


class ViasPhoneNumber2Dict(TypedDict):
    phone_country_code: NotRequired[str]
    phone_number: NotRequired[str]
    phone_type: NotRequired[PhoneTypeOrStr]
