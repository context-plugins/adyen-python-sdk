from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type45 import Type45OrStr
from .pix_pay_by_bank_risk_signals import PixPayByBankRiskSignals, PixPayByBankRiskSignalsDict


class StoredPaymentMethod5(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    issuer: Optional[str] = UNSET
    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    risk_signals: Optional[PixPayByBankRiskSignals] = Field(default=UNSET, alias="riskSignals")
    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Optional[Type45OrStr] = Field(default=UNSET, alias="type")
    """**paybybank_pix**"""


class StoredPaymentMethod5Dict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    device_id: NotRequired[str]
    issuer: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    risk_signals: NotRequired[PixPayByBankRiskSignals | PixPayByBankRiskSignalsDict]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type45OrStr]
