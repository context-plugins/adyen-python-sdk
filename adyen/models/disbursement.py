from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .capital_balance import CapitalBalance, CapitalBalanceDict
from .disbursement_repayment2 import DisbursementRepayment2, DisbursementRepayment2Dict
from .fee22 import Fee22, Fee22Dict
from .funds_collection import FundsCollection, FundsCollectionDict


class Disbursement(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder that received the disbursement."""

    amount: Amount17
    """Contains information about the amount of the disbursement."""

    balance_account_id: str = Field(alias="balanceAccountId")
    """The unique identifier of the balance account that received the disbursement."""

    balances: CapitalBalance
    """Contains information about the balances of the disbursement."""

    fee: Fee22
    """Contains information about the fee that your user must pay for the disbursement."""

    funds_collections: Optional[list[FundsCollection]] = Field(default=UNSET, alias="fundsCollections")
    """Contains information about the accounts that Adyen uses to collect funds related to repayments."""

    grant_id: str = Field(alias="grantId")
    """The unique identifier of the grant related to the disbursement."""

    id: str
    """The unique identifier of the disbursement."""

    repayment: DisbursementRepayment2
    """Contains information about the basis points configured for repaying the disbursement."""


class DisbursementDict(TypedDict):
    account_holder_id: str
    amount: Amount17Dict
    balance_account_id: str
    balances: CapitalBalanceDict
    fee: Fee22Dict
    funds_collections: NotRequired[list[FundsCollectionDict]]
    grant_id: str
    id: str
    repayment: DisbursementRepayment2Dict
