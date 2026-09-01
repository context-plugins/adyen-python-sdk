from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type83(str, Enum):
    """The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**,
    **bankTransfer**."""

    PAYMENT = "payment"
    CAPTURE = "capture"
    CAPTURE_REVERSAL = "captureReversal"
    REFUND = "refund"
    REFUND_REVERSAL = "refundReversal"
    CHARGEBACK = "chargeback"
    CHARGEBACK_CORRECTION = "chargebackCorrection"
    CHARGEBACK_REVERSAL = "chargebackReversal"
    CHARGEBACK_REVERSAL_CORRECTION = "chargebackReversalCorrection"
    SECOND_CHARGEBACK = "secondChargeback"
    SECOND_CHARGEBACK_CORRECTION = "secondChargebackCorrection"
    ATM_WITHDRAWAL = "atmWithdrawal"
    ATM_WITHDRAWAL_REVERSAL = "atmWithdrawalReversal"
    INTERNAL_TRANSFER = "internalTransfer"
    INTERNAL_DIRECT_DEBIT = "internalDirectDebit"
    MANUAL_CORRECTION = "manualCorrection"
    INVOICE_DEDUCTION = "invoiceDeduction"
    DEPOSIT_CORRECTION = "depositCorrection"
    RESERVE_ADJUSTMENT = "reserveAdjustment"
    BANK_TRANSFER = "bankTransfer"
    BANK_DIRECT_DEBIT = "bankDirectDebit"
    CARD_TRANSFER = "cardTransfer"
    MISC_COST = "miscCost"
    PAYMENT_COST = "paymentCost"
    FEE = "fee"
    LEFTOVER = "leftover"
    GRANT = "grant"
    CAPITAL_FUNDS_COLLECTION = "capitalFundsCollection"
    CASH_OUT_INSTRUCTION = "cashOutInstruction"
    CASHOUT_FEE = "cashoutFee"
    CASHOUT_REPAYMENT = "cashoutRepayment"
    CASHOUT_FUNDING = "cashoutFunding"
    REPAYMENT = "repayment"
    INSTALLMENT = "installment"
    INSTALLMENT_REVERSAL = "installmentReversal"
    BALANCE_ADJUSTMENT = "balanceAdjustment"
    BALANCE_ROLLOVER = "balanceRollover"
    BALANCE_MIGRATION = "balanceMigration"

    __str__ = str.__str__


Type83OrStr: TypeAlias = Annotated[Type83 | str, open_enum_validator(Type83)]
