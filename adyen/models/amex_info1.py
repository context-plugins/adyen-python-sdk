from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_level import ServiceLevelOrStr


class AmexInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **amex**. For merchants operating in Australia, New Zealand & Canada, JCB and
    American Express are automatically requested together."""

    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """Merchant ID (MID) number. Format: 10 numeric characters.
     You must provide this field when you request ``gatewayContract`` or ``paymentDesignatorContract`` service
        levels."""

    reuse_mid_number: Optional[bool] = Field(default=UNSET, alias="reuseMidNumber")
    """Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method. This is only
    applicable for ``gatewayContract`` and ``paymentDesignatorContract`` service levels. The default value is
    **false**."""

    service_level: ServiceLevelOrStr = Field(alias="serviceLevel")
    """Specifies the service level (settlement type) of this payment method. Possible values:
    * **noContract**: Adyen holds the contract with American Express.
    * **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your
        sub-merchant directly.
    * **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts."""


class AmexInfo1Dict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: NotRequired[bool]
    service_level: ServiceLevelOrStr
