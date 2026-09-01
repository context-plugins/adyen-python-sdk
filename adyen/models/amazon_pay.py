from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type4 import Type4OrStr


class AmazonPay(SdkBaseModel):
    amazon_pay_token: Optional[str] = Field(default=UNSET, alias="amazonPayToken")
    """This is the ``amazonPayToken`` that you obtained from the `Get Checkout Session
    <https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-session>`__
    response. This token is used for API only integration specifically."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    checkout_session_id: Optional[str] = Field(default=UNSET, alias="checkoutSessionId")
    """The ``checkoutSessionId`` is used to identify the checkout session at the Amazon Pay side. This field is required
    only for drop-in and components integration, where it replaces the amazonPayToken."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type4OrStr] = Field(default=UNSET, alias="type")
    """**amazonpay**"""


class AmazonPayDict(TypedDict):
    amazon_pay_token: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    checkout_session_id: NotRequired[str]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type4OrStr]
