from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AmexResponseInfo(SdkBaseModel):
    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """Merchant ID (MID) number."""

    reuse_mid_number: Optional[bool] = Field(default=UNSET, alias="reuseMidNumber")
    """Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method."""

    service_level: Optional[str] = Field(default=UNSET, alias="serviceLevel")
    """The service level (settlement type) of this payment method. Possible values:
    * **noContract**: Adyen holds the contract with American Express.
    * **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your
        sub-merchant directly.
    * **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts."""


class AmexResponseInfoDict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: NotRequired[bool]
    service_level: NotRequired[str]
