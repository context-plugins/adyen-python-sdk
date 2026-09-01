from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type30 import Type30OrStr


class EftDirectDebit(SdkBaseModel):
    bank_account_number: Optional[str] = Field(default=UNSET, alias="bankAccountNumber")
    """The bank account number (without separators)."""

    bank_code: Optional[str] = Field(default=UNSET, alias="bankCode")
    """The financial institution code."""

    bank_location_id: Optional[str] = Field(default=UNSET, alias="bankLocationId")
    """The bank routing number of the account."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The name of the bank account holder. If you submit a name with non-Latin characters, we automatically replace
    some of them with corresponding Latin characters to meet the FATF recommendations. For example:
    * χ12 is converted to ch12.
    * üA is converted to euA.
    * Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.
    After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one
    of them must be a valid Latin character (A-Z, a-z). For example:
    * John17 - allowed.
    * J17 - allowed.
    * 171 - not allowed.
    * John-7 - allowed.
    > If provided details don't match the required format, the response returns the error message: 203 'Invalid bank
        account holder name'."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Optional[Type30OrStr] = Field(default=UNSET, alias="type")
    """**eft**"""


class EftDirectDebitDict(TypedDict):
    bank_account_number: NotRequired[str]
    bank_code: NotRequired[str]
    bank_location_id: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    owner_name: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type30OrStr]
