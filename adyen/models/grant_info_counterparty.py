from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GrantInfoCounterparty(SdkBaseModel):
    """Contains the details of the party that receives the grant."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The identifier of the balance account that belongs to the receiving account holder."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The identifier of the transfer instrument that belongs to the legal entity of the account holder."""


class GrantInfoCounterpartyDict(TypedDict):
    balance_account_id: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
