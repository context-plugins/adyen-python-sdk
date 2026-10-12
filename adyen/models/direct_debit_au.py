from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type22 import Type22, Type22OrStr


class DirectDebitAu(SdkBaseModel):
    bank_account_number: Optional[str] = Field(default=UNSET, alias="bankAccountNumber")
    """The shopper's banking account number used to complete payment."""

    bank_branch_code: Optional[str] = Field(default=UNSET, alias="bankBranchCode")
    """The shopper's BSB (their bank's branch code) number used to complete payment."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    holder_name: str = Field(alias="holderName")
    """The name of the bank account holder."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Type22OrStr = Field(default=Type22.DIRECTDEBIT_AU, alias="type")
    """**directdebit_AU**"""


class DirectDebitAuDict(TypedDict):
    bank_account_number: NotRequired[str]
    bank_branch_code: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    holder_name: str
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type22OrStr]
