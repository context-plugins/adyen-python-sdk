from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address8(SdkBaseModel):
    city: Optional[str] = UNSET
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    street_address: Optional[str] = Field(default=UNSET, alias="streetAddress")
    street_address2: Optional[str] = Field(default=UNSET, alias="streetAddress2")


class Address8Dict(TypedDict):
    city: NotRequired[str]
    country_code: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
    street_address: NotRequired[str]
    street_address2: NotRequired[str]
