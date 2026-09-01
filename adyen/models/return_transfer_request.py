from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class ReturnTransferRequest(SdkBaseModel):
    amount: Amount17
    """Contains information about the amount to be returned."""

    reference: Optional[str] = UNSET
    """Your internal reference for the return. If you don't provide this in the request, Adyen generates a unique
    reference. This reference is used in all communication with you about the instruction status.

    We recommend using a unique value per instruction. If you need to provide multiple references for a transaction,
    separate them with hyphens ("-")."""


class ReturnTransferRequestDict(TypedDict):
    amount: Amount17 | Amount17Dict
    reference: NotRequired[str]
