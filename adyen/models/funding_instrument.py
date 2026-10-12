from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_identification2 import CardIdentification2, CardIdentification2Dict
from .enums.source_of_funds import SourceOfFundsOrStr


class FundingInstrument(SdkBaseModel):
    card_identification: Optional[CardIdentification2] = Field(default=UNSET, alias="cardIdentification")
    """Card details used for the transfer, such as the Primary Account Number (PAN) or stored payment method ID.
    Required if ``sourceOfFunds`` is **DEBIT**. Provide either:
     - ``storedPaymentMethodId`` or
     - ``expiryMonth``, ``expiryYear``, and ``number``."""

    network_payment_reference: Optional[str] = Field(default=UNSET, alias="networkPaymentReference")
    """The unique reference assigned by the card network for the pay-in transaction."""

    reference: Optional[str] = UNSET
    """Your internal reference that identifies this funding instrument. Required if ``sourceOfFunds`` is
    **DEPOSIT_ACCOUNT**."""

    source_of_funds: Optional[SourceOfFundsOrStr] = Field(default=UNSET, alias="sourceOfFunds")
    """Indicates where the funds used for the transfer originated. Possible values are:
    - **DEBIT** for card-to-card transfers.
    - **DEPOSIT_ACCOUNT** for wallet-to-card transfers."""


class FundingInstrumentDict(TypedDict):
    card_identification: NotRequired[CardIdentification2Dict]
    network_payment_reference: NotRequired[str]
    reference: NotRequired[str]
    source_of_funds: NotRequired[SourceOfFundsOrStr]
