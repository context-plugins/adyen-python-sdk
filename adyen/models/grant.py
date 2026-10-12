from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capital_balance import CapitalBalance, CapitalBalanceDict
from .grant_counterparty import GrantCounterparty, GrantCounterpartyDict
from .status25 import Status25, Status25Dict


class Grant(SdkBaseModel):
    balances: CapitalBalance
    """Contains information about the balances of the grant."""

    counterparty: Optional[GrantCounterparty] = UNSET
    """Contains the details of the party that receives the grant."""

    grant_account_id: str = Field(alias="grantAccountId")
    """The unique identifier of the grant account that tracks this grant."""

    grant_offer_id: str = Field(alias="grantOfferId")
    """The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant."""

    id: str
    """The unique identifier of the grant reference."""

    status: Status25
    """Contains the status of the grant."""


class GrantDict(TypedDict):
    balances: CapitalBalanceDict
    counterparty: NotRequired[GrantCounterpartyDict]
    grant_account_id: str
    grant_offer_id: str
    id: str
    status: Status25Dict
