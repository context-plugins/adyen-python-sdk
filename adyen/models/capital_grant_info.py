from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .grant_info_counterparty2 import GrantInfoCounterparty2, GrantInfoCounterparty2Dict


class CapitalGrantInfo(SdkBaseModel):
    counterparty: Optional[GrantInfoCounterparty2] = UNSET
    """An object containing the details of the receiving party of the grant."""

    grant_account_id: str = Field(alias="grantAccountId")
    """The identifier of the grant account used for the grant."""

    grant_offer_id: str = Field(alias="grantOfferId")
    """The identifier of the grant offer that has been selected and from which the grant details will be used."""


class CapitalGrantInfoDict(TypedDict):
    counterparty: NotRequired[GrantInfoCounterparty2Dict]
    grant_account_id: str
    grant_offer_id: str
