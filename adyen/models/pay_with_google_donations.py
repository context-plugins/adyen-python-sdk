from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type26 import Type26, Type26OrStr


class PayWithGoogleDonations(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    google_pay_token: str = Field(alias="googlePayToken")
    """The ``token`` that you obtained from the `Google Pay API
    <https://developers.google.com/pay/api/web/reference/response-objects#PaymentData>`__ ``PaymentData`` response."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    three_ds2_sdk_version: Optional[str] = Field(default=UNSET, alias="threeDS2SdkVersion")
    """Required for mobile integrations. Version of the 3D Secure 2 mobile SDK."""

    type_: Type26OrStr = Field(default=Type26.PAYWITHGOOGLE, alias="type")
    """**paywithgoogle**"""


class PayWithGoogleDonationsDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    google_pay_token: str
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    three_ds2_sdk_version: NotRequired[str]
    type_: NotRequired[Type26OrStr]
