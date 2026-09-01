from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MerchantDetails(SdkBaseModel):
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """2-letter ISO 3166 country code of the card acceptor location.
    > This parameter is required for the merchants who don't use Adyen as the payment authorisation gateway."""

    enrolled_in3_d_secure: Optional[bool] = Field(default=UNSET, alias="enrolledIn3DSecure")
    """If true, indicates that the merchant is enrolled in 3D Secure for the card network."""

    mcc: Optional[str] = UNSET
    """The merchant category code (MCC) is a four-digit number which relates to a particular market segment. This code
    reflects the predominant activity that is conducted by the merchant.

    The list of MCCs can be found `here <https://en.wikipedia.org/wiki/Merchant_category_code>`__."""


class MerchantDetailsDict(TypedDict):
    country_code: NotRequired[str]
    enrolled_in3_d_secure: NotRequired[bool]
    mcc: NotRequired[str]
