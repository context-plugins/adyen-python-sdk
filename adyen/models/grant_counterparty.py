from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GrantCounterparty(SdkBaseModel):
    """Contains the details of the party that receives the grant."""

    account_holder_id: Optional[str] = Field(default=UNSET, alias="accountHolderId")
    """The identifier of the receiving account holder."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The identifier of the balance account that belongs to the receiving account holder."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The identifier of the transfer instrument that belongs to the legal entity of the account holder."""


class GrantCounterpartyDict(TypedDict):
    account_holder_id: NotRequired[str]
    balance_account_id: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
