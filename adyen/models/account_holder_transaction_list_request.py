from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.transaction_status import TransactionStatusOrStr
from .transaction_list_for_account import TransactionListForAccount, TransactionListForAccountDict


class AccountHolderTransactionListRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder that owns the account(s) of which retrieve the transaction list."""

    transaction_lists_per_account: Optional[list[TransactionListForAccount]] = Field(
        default=UNSET, alias="transactionListsPerAccount"
    )
    """A list of accounts to include in the transaction list. If left blank, the last fifty (50) transactions for all
    accounts of the account holder will be included."""

    transaction_statuses: Optional[list[TransactionStatusOrStr]] = Field(default=UNSET, alias="transactionStatuses")
    """A list of statuses to include in the transaction list. If left blank, all transactions will be included.
    >Permitted values: >* ``PendingCredit`` - a pending balance credit. >* ``CreditFailed`` - a pending credit failure;
    the balance will not be credited. >* ``Credited`` - a credited balance. >* ``PendingDebit`` - a pending balance
    debit (e.g., a refund). >* ``CreditClosed`` - a pending credit closed; the balance will not be credited. >*
    ``CreditSuspended`` - a pending credit closed; the balance will not be credited. >* ``DebitFailed`` - a pending
    debit failure; the balance will not be debited. >* ``Debited`` - a debited balance (e.g., a refund). >*
    ``DebitReversedReceived`` - a pending refund reversal. >* ``DebitedReversed`` - a reversed refund. >*
    ``ChargebackReceived`` - a received chargeback request. >* ``Chargeback`` - a processed chargeback. >*
    ``ChargebackReversedReceived`` - a pending chargeback reversal. >* ``ChargebackReversed`` - a reversed chargeback.
    >* ``Converted`` - converted. >* ``ManualCorrected`` - manual booking/adjustment by Adyen. >* ``Payout`` - a payout.
    >* ``PayoutReversed`` - a reversed payout. >* ``PendingFundTransfer`` - a pending transfer of funds from one account
    to another. >* ``FundTransfer`` - a transfer of funds from one account to another."""


class AccountHolderTransactionListRequestDict(TypedDict):
    account_holder_code: str
    transaction_lists_per_account: NotRequired[list[TransactionListForAccountDict]]
    transaction_statuses: NotRequired[list[TransactionStatusOrStr]]
