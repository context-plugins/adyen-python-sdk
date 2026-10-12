from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.payment_type1 import PaymentType1OrStr
from .instalment1 import Instalment1, Instalment1Dict
from .payment_instrument_data import PaymentInstrumentData, PaymentInstrumentDataDict
from .transaction_idtype import TransactionIdtype, TransactionIdtypeDict


class PaymentData(SdkBaseModel):
    payment_type: Optional[PaymentType1OrStr] = Field(default=UNSET, alias="PaymentType")
    """Type of payment transaction. Elements requested by the Sale System that are related to the payment only. Possible
    values:
    * **CashAdvance**
    * **CashDeposit**
    * **Completion**
    * **FirstReservation**
    * **Instalment**
    * **IssuerInstalment**
    * **Normal**
    * **OneTimeReservation**
    * **PaidOut**
    * **Recurring**
    * **Refund**
    * **UpdateReservation**"""

    split_payment_flag: bool = Field(default=False, alias="SplitPaymentFlag")
    """Indicates if the payment of the Sale transaction is split. Allows the POI to decline payment means that cannot
    accept split payment."""

    requested_validity_date: Optional[Date] = Field(default=UNSET, alias="RequestedValidityDate")
    """Requested validity date for the reservation. Allows a specific period for the reservation according to the need
    of the Merchant for the first reservation and the reservation updates as well."""

    card_acquisition_reference: Optional[TransactionIdtype] = Field(default=UNSET, alias="CardAcquisitionReference")
    """Identification of a transaction for the Sale System or the POI System."""

    instalment: Optional[Instalment1] = Field(default=UNSET, alias="Instalment")
    """Information related an instalment transaction. To request an instalment to the issuer, or to make individual
    instalments of a payment transaction."""

    payment_instrument_data: Optional[PaymentInstrumentData] = Field(default=UNSET, alias="PaymentInstrumentData")
    """Data related to the instrument of payment for the transaction. Sent in the result of the payment transaction. For
    a card, it could also be sent in the ``CardAcquisition`` response, to be processed by the Sale System."""


class PaymentDataDict(TypedDict):
    payment_type: NotRequired[PaymentType1OrStr]
    split_payment_flag: NotRequired[bool]
    requested_validity_date: NotRequired[Date]
    card_acquisition_reference: NotRequired[TransactionIdtypeDict]
    instalment: NotRequired[Instalment1Dict]
    payment_instrument_data: NotRequired[PaymentInstrumentDataDict]
