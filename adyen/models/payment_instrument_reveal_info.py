from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .expiry2 import Expiry2, Expiry2Dict


class PaymentInstrumentRevealInfo(SdkBaseModel):
    cvc: str
    """The CVC2 value of the card."""

    expiration: Expiry2
    """The expiration date of the card."""

    pan: str
    """The primary account number (PAN) of the card."""


class PaymentInstrumentRevealInfoDict(TypedDict):
    cvc: str
    expiration: Expiry2 | Expiry2Dict
    pan: str
