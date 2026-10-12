from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount import Amount, AmountDict
from .bank_account_detail import BankAccountDetail, BankAccountDetailDict
from .enums.transaction_status1 import TransactionStatus1OrStr


class Transaction1(SdkBaseModel):
    amount: Optional[Amount] = UNSET
    """The amount of the transaction."""

    bank_account_detail: Optional[BankAccountDetail] = Field(default=UNSET, alias="bankAccountDetail")
    """The details of the bank account to where a payout was made."""

    capture_merchant_reference: Optional[str] = Field(default=UNSET, alias="captureMerchantReference")
    """The merchant reference of a related capture."""

    capture_psp_reference: Optional[str] = Field(default=UNSET, alias="capturePspReference")
    """The psp reference of a related capture."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date on which the transaction was performed."""

    description: Optional[str] = UNSET
    """A description of the transaction."""

    destination_account_code: Optional[str] = Field(default=UNSET, alias="destinationAccountCode")
    """The code of the account to which funds were credited during an outgoing fund transfer."""

    dispute_psp_reference: Optional[str] = Field(default=UNSET, alias="disputePspReference")
    """The psp reference of the related dispute."""

    dispute_reason_code: Optional[str] = Field(default=UNSET, alias="disputeReasonCode")
    """The reason code of a dispute."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The merchant reference of a transaction."""

    payment_psp_reference: Optional[str] = Field(default=UNSET, alias="paymentPspReference")
    """The psp reference of the related authorisation or transfer."""

    payout_psp_reference: Optional[str] = Field(default=UNSET, alias="payoutPspReference")
    """The psp reference of the related payout."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The psp reference of a transaction."""

    source_account_code: Optional[str] = Field(default=UNSET, alias="sourceAccountCode")
    """The code of the account from which funds were debited during an incoming fund transfer."""

    transaction_status: Optional[TransactionStatus1OrStr] = Field(default=UNSET, alias="transactionStatus")
    """The status of the transaction. >Permitted values: ``PendingCredit``, ``CreditFailed``, ``CreditClosed``,
    ``CreditSuspended``, ``Credited``, ``Converted``, ``PendingDebit``, ``DebitFailed``, ``Debited``,
    ``DebitReversedReceived``, ``DebitedReversed``, ``ChargebackReceived``, ``Chargeback``,
    ``ChargebackReversedReceived``, ``ChargebackReversed``, ``Payout``, ``PayoutReversed``, ``FundTransfer``,
    ``PendingFundTransfer``, ``ManualCorrected``."""

    transfer_code: Optional[str] = Field(default=UNSET, alias="transferCode")
    """The transfer code of the transaction."""


class Transaction1Dict(TypedDict):
    amount: NotRequired[AmountDict]
    bank_account_detail: NotRequired[BankAccountDetailDict]
    capture_merchant_reference: NotRequired[str]
    capture_psp_reference: NotRequired[str]
    creation_date: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    destination_account_code: NotRequired[str]
    dispute_psp_reference: NotRequired[str]
    dispute_reason_code: NotRequired[str]
    merchant_reference: NotRequired[str]
    payment_psp_reference: NotRequired[str]
    payout_psp_reference: NotRequired[str]
    psp_reference: NotRequired[str]
    source_account_code: NotRequired[str]
    transaction_status: NotRequired[TransactionStatus1OrStr]
    transfer_code: NotRequired[str]
