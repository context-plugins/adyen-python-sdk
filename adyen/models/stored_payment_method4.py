from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type44 import Type44OrStr
from .pix_recurring import PixRecurring, PixRecurringDict


class StoredPaymentMethod4(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    pix_recurring: Optional[PixRecurring] = Field(default=UNSET, alias="pixRecurring")
    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Optional[Type44OrStr] = Field(default=UNSET, alias="type")
    """The payment method type."""


class StoredPaymentMethod4Dict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    pix_recurring: NotRequired[PixRecurring | PixRecurringDict]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type44OrStr]
