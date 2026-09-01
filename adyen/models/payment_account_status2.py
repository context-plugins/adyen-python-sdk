from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_acquirer_data import PaymentAcquirerData, PaymentAcquirerDataDict
from .payment_instrument_data import PaymentInstrumentData, PaymentInstrumentDataDict


class PaymentAccountStatus2(SdkBaseModel):
    """Data related to the result of a Balance Inquiry request. If BalanceInquiryRequest. PaymentAccount present."""

    payment_instrument_data: Optional[PaymentInstrumentData] = Field(default=UNSET, alias="PaymentInstrumentData")
    """Data related to the instrument of payment for the transaction. Sent in the result of the payment transaction. For
    a card, it could also be sent in the ``CardAcquisition`` response, to be processed by the Sale System."""

    current_balance: Optional[float] = Field(default=UNSET, alias="CurrentBalance")
    """Balance of an account after processing of the transaction."""

    currency: Optional[str] = Field(default=UNSET, alias="Currency")
    """Currency of a monetary amount."""

    payment_acquirer_data: Optional[PaymentAcquirerData] = Field(default=UNSET, alias="PaymentAcquirerData")
    """Data related to the response from the payment Acquirer."""


class PaymentAccountStatus2Dict(TypedDict):
    payment_instrument_data: NotRequired[PaymentInstrumentData | PaymentInstrumentDataDict]
    current_balance: NotRequired[float]
    currency: NotRequired[str]
    payment_acquirer_data: NotRequired[PaymentAcquirerData | PaymentAcquirerDataDict]
