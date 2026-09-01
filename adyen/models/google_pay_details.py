from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type24 import Type24OrStr


class GooglePayDetails(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    google_pay_card_network: Optional[str] = Field(default=UNSET, alias="googlePayCardNetwork")
    """The selected payment card network."""

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

    type_: Optional[Type24OrStr] = Field(default=UNSET, alias="type")
    """**googlepay**, **paywithgoogle**"""


class GooglePayDetailsDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    google_pay_card_network: NotRequired[str]
    google_pay_token: str
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    three_ds2_sdk_version: NotRequired[str]
    type_: NotRequired[Type24OrStr]
