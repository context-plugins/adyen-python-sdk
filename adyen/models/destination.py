from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Destination(SdkBaseModel):
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ or three-letter `ISO
    3166-1 alpha-3 country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ for the destination address.
    * Encoding: ASCII
    * Min length: 2 characters
    * Max length: 3 characters
    * **additionalData key:** ``enhancedSchemeData.destinationCountryCode``"""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code of the destination address.
    * Encoding: ASCII
    * Max length: 10 characters
    * Must not start with a space.
    * For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
    * For Canada, it must be in 6 digits format. For example, M4B 1G5.
    * **additionalData key:** ``enhancedSchemeData.destinationPostalCode``"""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The state or province code of the destination address.
    * Encoding: ASCII
    * Max length: 3 characters
    * Must not start with a space.
    * **additionalData key:** ``enhancedSchemeData.destinationStateProvinceCode``"""


class DestinationDict(TypedDict):
    country_code: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
