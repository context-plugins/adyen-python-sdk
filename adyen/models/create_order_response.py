from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount12 import Amount12, Amount12Dict
from .amount23 import Amount23, Amount23Dict
from .fraud_result1 import FraudResult1, FraudResult1Dict


class CreateOrderResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some data fields are included only if you select them first:
    Go to **Customer Area** > **Developers** > **Additional data**."""

    amount: Amount12
    """The initial amount of the order."""

    expires_at: str = Field(alias="expiresAt")
    """The date that the order will expire."""

    fraud_result: Optional[FraudResult1] = Field(default=UNSET, alias="fraudResult")
    """The fraud result properties of the payment."""

    order_data: str = Field(alias="orderData")
    """The encrypted data that will be used by merchant for adding payments to the order."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it
    when communicating with us about this request."""

    reference: Optional[str] = UNSET
    """The reference provided by merchant for creating the order."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's
    mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response
    includes ``resultCode`` and ``refusalReason`` values.

    For more information, see `Refusal reasons <https://docs.adyen.com/development-resources/refusal-reasons>`__."""

    remaining_amount: Amount23 = Field(alias="remainingAmount")
    """The remaining amount in the order."""

    result_code: Literal["Success"] = Field(default="Success", alias="resultCode")
    """The result of the order creation request.
     The value is always **Success**."""


class CreateOrderResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    amount: Amount12Dict
    expires_at: str
    fraud_result: NotRequired[FraudResult1Dict]
    order_data: str
    psp_reference: NotRequired[str]
    reference: NotRequired[str]
    refusal_reason: NotRequired[str]
    remaining_amount: Amount23Dict
    result_code: Literal["Success"]
