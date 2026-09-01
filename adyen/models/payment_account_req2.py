from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_type12 import AccountType12OrStr
from .payment_instrument_data import PaymentInstrumentData, PaymentInstrumentDataDict
from .transaction_idtype import TransactionIdtype, TransactionIdtypeDict


class PaymentAccountReq2(SdkBaseModel):
    """Data related to the account pointed by the payment card."""

    account_type: Optional[AccountType12OrStr] = Field(default=UNSET, alias="AccountType")
    """Type of cardholder account used for the transaction. Allows a cardholder to select the type of account used for
    the transaction. Possible values:
    * **CardTotals**
    * **Checking**
    * **CreditCard**
    * **Default**
    * **EpurseCard**
    * **Investment**
    * **Savings**
    * **Universal**"""

    card_acquisition_reference: Optional[TransactionIdtype] = Field(default=UNSET, alias="CardAcquisitionReference")
    """Identification of a transaction for the Sale System or the POI System."""

    payment_instrument_data: Optional[PaymentInstrumentData] = Field(default=UNSET, alias="PaymentInstrumentData")
    """Data related to the instrument of payment for the transaction. Sent in the result of the payment transaction. For
    a card, it could also be sent in the ``CardAcquisition`` response, to be processed by the Sale System."""


class PaymentAccountReq2Dict(TypedDict):
    account_type: NotRequired[AccountType12OrStr]
    card_acquisition_reference: NotRequired[TransactionIdtype | TransactionIdtypeDict]
    payment_instrument_data: NotRequired[PaymentInstrumentData | PaymentInstrumentDataDict]
