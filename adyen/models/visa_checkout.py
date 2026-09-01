from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type55 import Type55OrStr


class VisaCheckout(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type55OrStr] = Field(default=UNSET, alias="type")
    """**visacheckout**"""

    visa_checkout_call_id: str = Field(alias="visaCheckoutCallId")
    """The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa
    Click to Pay, you will receive a Visa Click to Pay Call ID."""


class VisaCheckoutDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type55OrStr]
    visa_checkout_call_id: str
