from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account11 import BankAccount11, BankAccount11Dict


class Counterparty(SdkBaseModel):
    bank_account: Optional[BankAccount11] = Field(default=UNSET, alias="bankAccount")
    """Contains information about the bank account."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The unique identifier of the `transfer instrument
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__."""


class CounterpartyDict(TypedDict):
    bank_account: NotRequired[BankAccount11 | BankAccount11Dict]
    transfer_instrument_id: NotRequired[str]
