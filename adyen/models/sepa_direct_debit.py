from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type51 import Type51, Type51OrStr


class SepaDirectDebit(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    due_date: Optional[str] = Field(default=UNSET, alias="dueDate")
    """The date that the the shopper's bank account is charged."""

    iban: str
    """The International Bank Account Number (IBAN)."""

    owner_name: str = Field(alias="ownerName")
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

    type_: Type51OrStr = Field(default=Type51.SEPADIRECTDEBIT, alias="type")
    """**sepadirectdebit**"""


class SepaDirectDebitDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    due_date: NotRequired[str]
    iban: str
    owner_name: str
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
    type_: NotRequired[Type51OrStr]
