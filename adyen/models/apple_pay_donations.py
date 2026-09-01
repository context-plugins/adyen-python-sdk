from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type7 import Type7OrStr


class ApplePayDonations(SdkBaseModel):
    apple_pay_token: str = Field(alias="applePayToken")
    """The stringified and base64 encoded ``paymentData`` you retrieved from the Apple framework."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Optional[Type7OrStr] = Field(default=UNSET, alias="type")
    """**applepay**"""


class ApplePayDonationsDict(TypedDict):
    apple_pay_token: str
    checkout_attempt_id: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type7OrStr]
