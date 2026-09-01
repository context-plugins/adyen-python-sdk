from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type10 import Type10OrStr


class BacsDirectDebit(SdkBaseModel):
    bank_account_number: Optional[str] = Field(default=UNSET, alias="bankAccountNumber")
    """The bank account number (without separators)."""

    bank_location_id: Optional[str] = Field(default=UNSET, alias="bankLocationId")
    """The bank routing number of the account."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the bank account holder."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The unique identifier of your user's verified transfer instrument, which you can use to top up their balance
    accounts."""

    type_: Optional[Type10OrStr] = Field(default=UNSET, alias="type")
    """**directdebit_GB**"""


class BacsDirectDebitDict(TypedDict):
    bank_account_number: NotRequired[str]
    bank_location_id: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    holder_name: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
    type_: NotRequired[Type10OrStr]
