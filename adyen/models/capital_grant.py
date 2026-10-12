from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .capital_balance import CapitalBalance, CapitalBalanceDict
from .enums.status14 import Status14OrStr
from .fee4 import Fee4, Fee4Dict
from .grant_counterparty2 import GrantCounterparty2, GrantCounterparty2Dict
from .repayment import Repayment, RepaymentDict


class CapitalGrant(SdkBaseModel):
    amount: Optional[Amount17] = UNSET
    """An object containing the amount of the grant, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    balances: CapitalBalance
    """An object containing the details of the existing grant."""

    counterparty: Optional[GrantCounterparty2] = UNSET
    """An object containing the details of the receiving party of the grant."""

    fee: Optional[Fee4] = UNSET
    """An object containing the fee currency and value, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    grant_account_id: str = Field(alias="grantAccountId")
    """The identifier of the grant account used for the grant."""

    grant_offer_id: str = Field(alias="grantOfferId")
    """The identifier of the grant offer that has been selected and from which the grant details will be used."""

    id: str
    """The identifier of the grant reference."""

    repayment: Optional[Repayment] = UNSET
    """An object containing the details of the 30-day repayment threshold."""

    status: Status14OrStr
    """The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**, **WrittenOff**,
    **Failed**, **Revoked**."""


class CapitalGrantDict(TypedDict):
    amount: NotRequired[Amount17Dict]
    balances: CapitalBalanceDict
    counterparty: NotRequired[GrantCounterparty2Dict]
    fee: NotRequired[Fee4Dict]
    grant_account_id: str
    grant_offer_id: str
    id: str
    repayment: NotRequired[RepaymentDict]
    status: Status14OrStr
