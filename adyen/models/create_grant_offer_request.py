from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class CreateGrantOfferRequest(SdkBaseModel):
    amount: Amount17
    """The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static
    offer."""


class CreateGrantOfferRequestDict(TypedDict):
    amount: Amount17 | Amount17Dict
