from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount8 import Amount8, Amount8Dict
from .amount9 import Amount9, Amount9Dict
from .enums.result_code import ResultCodeOrStr
from .fraud_result1 import FraudResult1, FraudResult1Dict


class BalanceCheckResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some data fields are included only if you select them first:
    Go to **Customer Area** > **Developers** > **Additional data**."""

    balance: Amount8
    """The balance for the payment method."""

    fraud_result: Optional[FraudResult1] = Field(default=UNSET, alias="fraudResult")
    """The fraud result properties of the payment."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it
    when communicating with us about this request."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's
    mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response
    includes ``resultCode`` and ``refusalReason`` values.

    For more information, see `Refusal reasons <https://docs.adyen.com/development-resources/refusal-reasons>`__."""

    result_code: ResultCodeOrStr = Field(alias="resultCode")
    """The result of the cancellation request.

    Possible values:

    * **Success** – Indicates that the balance check was successful.
    * **NotEnoughBalance** – Commonly indicates that the card did not have enough balance to pay the amount in the
        request, or that the currency of the balance on the card did not match the currency of the requested amount.
    * **Failed** – Indicates that the balance check failed."""

    transaction_limit: Optional[Amount9] = Field(default=UNSET, alias="transactionLimit")
    """The maximum spendable balance for a single transaction. Applicable to some gift cards."""


class BalanceCheckResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    balance: Amount8Dict
    fraud_result: NotRequired[FraudResult1Dict]
    psp_reference: NotRequired[str]
    refusal_reason: NotRequired[str]
    result_code: ResultCodeOrStr
    transaction_limit: NotRequired[Amount9Dict]
