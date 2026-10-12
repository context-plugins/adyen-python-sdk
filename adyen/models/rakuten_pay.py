from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type47 import Type47, Type47OrStr


class RakutenPay(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Type47OrStr = Field(default=Type47.RAKUTENPAY, alias="type")
    """**rakutenpay**"""


class RakutenPayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type47OrStr]
