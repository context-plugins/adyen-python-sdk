from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CashOutInfoCounterparty(SdkBaseModel):
    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The unique identifier of the counterparty transfer instrument.

    If you do not provide this field, the cashout funds remain in the instructing balance account after the cashout
    transfer is settled."""


class CashOutInfoCounterpartyDict(TypedDict):
    transfer_instrument_id: NotRequired[str]
