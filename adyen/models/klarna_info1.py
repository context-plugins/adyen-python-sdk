from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.region import RegionOrStr


class KlarnaInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **klarna** or its variant.

    You can use the following payment method ``type`` values for Klarna:
    * **klarna**: Klarna Pay Later
    * **klarna_account**: Klarna Pay over time
    * **klarna_paynow**: Klarna Pay now
    * **klarna_b2b**: `Billie via Klarna <https://docs.adyen.com/payment-methods/klarna/billie>`__"""

    auto_capture: Optional[bool] = Field(default=UNSET, alias="autoCapture")
    """Indicates the status of `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__.
    Default value: **false**."""

    dispute_email: str = Field(alias="disputeEmail")
    """The email address for disputes."""

    region: RegionOrStr
    """The region of operation. For example, **NA**, **EU**, **CH**, **AU**."""

    support_email: str = Field(alias="supportEmail")
    """The email address of merchant support."""


class KlarnaInfo1Dict(TypedDict):
    auto_capture: NotRequired[bool]
    dispute_email: str
    region: RegionOrStr
    support_email: str
