from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionStatus(str, Enum):
    BALANCE_NOT_PAID_OUT_TRANSFER = "BalanceNotPaidOutTransfer"
    BALANCE_PLATFORM_FUND_TRANSFER = "BalancePlatformFundTransfer"
    BALANCE_PLATFORM_SWEEP = "BalancePlatformSweep"
    BALANCE_PLATFORM_SWEEP_RETURNED = "BalancePlatformSweepReturned"
    CHARGEBACK = "Chargeback"
    CHARGEBACK_CORRECTION = "ChargebackCorrection"
    CHARGEBACK_CORRECTION_RECEIVED = "ChargebackCorrectionReceived"
    CHARGEBACK_RECEIVED = "ChargebackReceived"
    CHARGEBACK_REVERSED = "ChargebackReversed"
    CHARGEBACK_REVERSED_CORRECTION = "ChargebackReversedCorrection"
    CHARGEBACK_REVERSED_CORRECTION_RECEIVED = "ChargebackReversedCorrectionReceived"
    CHARGEBACK_REVERSED_RECEIVED = "ChargebackReversedReceived"
    CONVERTED = "Converted"
    CREDIT_CLOSED = "CreditClosed"
    CREDIT_FAILED = "CreditFailed"
    CREDIT_REVERSED = "CreditReversed"
    CREDIT_REVERSED_RECEIVED = "CreditReversedReceived"
    CREDIT_SUSPENDED = "CreditSuspended"
    CREDITED = "Credited"
    DEBIT_FAILED = "DebitFailed"
    DEBIT_REVERSED_RECEIVED = "DebitReversedReceived"
    DEBITED = "Debited"
    DEBITED_REVERSED = "DebitedReversed"
    DEPOSIT_CORRECTION_CREDITED = "DepositCorrectionCredited"
    DEPOSIT_CORRECTION_DEBITED = "DepositCorrectionDebited"
    DEPOSIT_CORRECTION_RECEIVED = "DepositCorrectionReceived"
    FEE = "Fee"
    FEE_RECEIVED = "FeeReceived"
    FUND_TRANSFER = "FundTransfer"
    FUND_TRANSFER_REVERSED = "FundTransferReversed"
    INVOICE_DEDUCTION_CREDITED = "InvoiceDeductionCredited"
    INVOICE_DEDUCTION_DEBITED = "InvoiceDeductionDebited"
    INVOICE_DEDUCTION_RECEIVED = "InvoiceDeductionReceived"
    MANUAL_CORRECTED = "ManualCorrected"
    MANUAL_CORRECTION_CREDITED = "ManualCorrectionCredited"
    MANUAL_CORRECTION_DEBITED = "ManualCorrectionDebited"
    MERCHANT_PAYIN = "MerchantPayin"
    MERCHANT_PAYIN_RECEIVED = "MerchantPayinReceived"
    MERCHANT_PAYIN_REVERSED = "MerchantPayinReversed"
    PAYOUT = "Payout"
    PAYOUT_REVERSED = "PayoutReversed"
    PENDING_CREDIT = "PendingCredit"
    PENDING_DEBIT = "PendingDebit"
    PENDING_FUND_TRANSFER = "PendingFundTransfer"
    RE_CREDITED = "ReCredited"
    RE_CREDITED_RECEIVED = "ReCreditedReceived"
    SECOND_CHARGEBACK = "SecondChargeback"
    SECOND_CHARGEBACK_CORRECTION = "SecondChargebackCorrection"
    SECOND_CHARGEBACK_CORRECTION_RECEIVED = "SecondChargebackCorrectionReceived"
    SECOND_CHARGEBACK_RECEIVED = "SecondChargebackReceived"

    __str__ = str.__str__


TransactionStatusOrStr: TypeAlias = Annotated[TransactionStatus | str, open_enum_validator(TransactionStatus)]
