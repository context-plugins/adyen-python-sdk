from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferNotificationMerchantData2(SdkBaseModel):
    """Contains information about the merchant."""

    acquirer_id: Optional[str] = Field(default=UNSET, alias="acquirerId")
    """The unique identifier of the merchant's acquirer."""

    city: Optional[str] = UNSET
    """The city where the merchant is located."""

    country: Optional[str] = UNSET
    """The country where the merchant is located."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The two-character country code of the merchant's location, in `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format."""

    mcc: Optional[str] = UNSET
    """The merchant category code."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant."""

    name: Optional[str] = UNSET
    """The name of the merchant's shop or service."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code of the merchant."""


class TransferNotificationMerchantData2Dict(TypedDict):
    acquirer_id: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    country_code: NotRequired[str]
    mcc: NotRequired[str]
    merchant_id: NotRequired[str]
    name: NotRequired[str]
    postal_code: NotRequired[str]
