from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class CalculateGrantOfferRequest(SdkBaseModel):
    amount: Amount17
    """The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a
    preliminary offer."""


class CalculateGrantOfferRequestDict(TypedDict):
    amount: Amount17Dict
