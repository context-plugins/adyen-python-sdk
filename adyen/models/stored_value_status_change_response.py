from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.result_code3 import ResultCode3OrStr


class StoredValueStatusChangeResponse(SdkBaseModel):
    auth_code: Optional[str] = Field(default=UNSET, alias="authCode")
    """Authorisation code:
    * When the payment is authorised, this field holds the authorisation code for the payment.
    * When the payment is not authorised, this field is empty."""

    current_balance: Optional[Amount] = Field(default=UNSET, alias="currentBalance")
    """The balance currently on the payment method."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character string reference associated with the transaction/request. This value is globally unique;
    quote it when communicating with us about this request."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """If the transaction is refused or an error occurs, this field holds Adyen's mapped reason for the refusal or a
    description of the error.

    When a transaction fails, the authorisation response includes ``resultCode`` and ``refusalReason`` values."""

    result_code: Optional[ResultCode3OrStr] = Field(default=UNSET, alias="resultCode")
    """The result of the payment. Possible values:

    * **Success** – The operation has been completed successfully.
    * **Refused** – The operation was refused. The reason is given in the ``refusalReason`` field.
    * **Error** – There was an error when the operation was processed. The reason is given in the ``refusalReason``
        field.
    * **NotEnoughBalance** – The amount on the payment method is lower than the amount given in the request. Only
        applicable to balance checks."""

    third_party_refusal_reason: Optional[str] = Field(default=UNSET, alias="thirdPartyRefusalReason")
    """Raw refusal reason received from the third party, where available"""


class StoredValueStatusChangeResponseDict(TypedDict):
    auth_code: NotRequired[str]
    current_balance: NotRequired[Amount | AmountDict]
    psp_reference: NotRequired[str]
    refusal_reason: NotRequired[str]
    result_code: NotRequired[ResultCode3OrStr]
    third_party_refusal_reason: NotRequired[str]
