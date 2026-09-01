from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_v31 import BankAccountV31, BankAccountV31Dict
from .card12 import Card12, Card12Dict
from .transfer_notification_merchant_data2 import (
    TransferNotificationMerchantData2,
    TransferNotificationMerchantData2Dict,
)


class TransferNotificationCounterParty2(SdkBaseModel):
    """The other party in the transfer."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the counterparty `balance account
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__."""

    bank_account: Optional[BankAccountV31] = Field(default=UNSET, alias="bankAccount")
    """Contains information about the counterparty bank account."""

    card: Optional[Card12] = UNSET
    """Contains information about the counterparty card."""

    merchant: Optional[TransferNotificationMerchantData2] = UNSET
    """Contains information about the merchant."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The unique identifier of the counterparty `transfer instrument
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__."""


class TransferNotificationCounterParty2Dict(TypedDict):
    balance_account_id: NotRequired[str]
    bank_account: NotRequired[BankAccountV31 | BankAccountV31Dict]
    card: NotRequired[Card12 | Card12Dict]
    merchant: NotRequired[TransferNotificationMerchantData2 | TransferNotificationMerchantData2Dict]
    transfer_instrument_id: NotRequired[str]
