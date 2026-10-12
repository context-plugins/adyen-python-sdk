from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type41 import Type41, Type41OrStr


class PayTo(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_account_identifier: Optional[str] = Field(default=UNSET, alias="shopperAccountIdentifier")
    """The shopper's banking details or payId reference, used to complete payment."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Type41OrStr = Field(default=Type41.PAYTO, alias="type")
    """**payto**"""


class PayToDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    shopper_account_identifier: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type41OrStr]
