from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status51(str, Enum):
    """The result of the transfer.

    For example:

    - **received**: an outgoing transfer request is created.
    - **refused**: the transfer request is rejected by Adyen for one of the following reasons:
      - Transfer limit exceeded.
      - Transaction rule requirements violated.
    - **authorised**: the transfer request is authorized and the funds are reserved.
    - **booked**: the funds are deducted from your user's balance account.
     - **failed**: the transfer is rejected by the counterparty's bank.
    - **returned**: the transfer is returned by the counterparty's bank."""

    APPROVAL_PENDING = "approvalPending"
    ATM_WITHDRAWAL = "atmWithdrawal"
    ATM_WITHDRAWAL_REVERSAL_PENDING = "atmWithdrawalReversalPending"
    ATM_WITHDRAWAL_REVERSED = "atmWithdrawalReversed"
    AUTH_ADJUSTMENT_AUTHORISED = "authAdjustmentAuthorised"
    AUTH_ADJUSTMENT_ERROR = "authAdjustmentError"
    AUTH_ADJUSTMENT_REFUSED = "authAdjustmentRefused"
    AUTHORISED = "authorised"
    BANK_TRANSFER = "bankTransfer"
    BANK_TRANSFER_PENDING = "bankTransferPending"
    BOOKED = "booked"
    BOOKING_PENDING = "bookingPending"
    CANCELLED = "cancelled"
    CAPTURE_PENDING = "capturePending"
    CAPTURE_REVERSAL_PENDING = "captureReversalPending"
    CAPTURE_REVERSED = "captureReversed"
    CAPTURED = "captured"
    CAPTURED_EXTERNALLY = "capturedExternally"
    CHARGEBACK = "chargeback"
    CHARGEBACK_EXTERNALLY = "chargebackExternally"
    CHARGEBACK_PENDING = "chargebackPending"
    CHARGEBACK_REVERSAL_PENDING = "chargebackReversalPending"
    CHARGEBACK_REVERSED = "chargebackReversed"
    CREDITED = "credited"
    DEPOSIT_CORRECTION = "depositCorrection"
    DEPOSIT_CORRECTION_PENDING = "depositCorrectionPending"
    DISPUTE = "dispute"
    DISPUTE_CLOSED = "disputeClosed"
    DISPUTE_EXPIRED = "disputeExpired"
    DISPUTE_NEEDS_REVIEW = "disputeNeedsReview"
    ERROR = "error"
    EXPIRED = "expired"
    FAILED = "failed"
    FEE = "fee"
    FEE_PENDING = "feePending"
    INTERCHANGE_ADJUSTED = "interchangeAdjusted"
    INTERNAL_TRANSFER = "internalTransfer"
    INTERNAL_TRANSFER_PENDING = "internalTransferPending"
    INVOICE_DEDUCTION = "invoiceDeduction"
    INVOICE_DEDUCTION_PENDING = "invoiceDeductionPending"
    MANUAL_CORRECTION_PENDING = "manualCorrectionPending"
    MANUALLY_CORRECTED = "manuallyCorrected"
    MATCHED_STATEMENT = "matchedStatement"
    MATCHED_STATEMENT_PENDING = "matchedStatementPending"
    MERCHANT_PAYIN = "merchantPayin"
    MERCHANT_PAYIN_PENDING = "merchantPayinPending"
    MERCHANT_PAYIN_REVERSED = "merchantPayinReversed"
    MERCHANT_PAYIN_REVERSED_PENDING = "merchantPayinReversedPending"
    MISC_COST = "miscCost"
    MISC_COST_PENDING = "miscCostPending"
    PAYMENT_COST = "paymentCost"
    PAYMENT_COST_PENDING = "paymentCostPending"
    PENDING = "pending"
    PENDING_APPROVAL = "pendingApproval"
    PENDING_EXECUTION = "pendingExecution"
    RECEIVED = "received"
    REFUND_PENDING = "refundPending"
    REFUND_REVERSAL_PENDING = "refundReversalPending"
    REFUND_REVERSED = "refundReversed"
    REFUNDED = "refunded"
    REFUNDED_EXTERNALLY = "refundedExternally"
    REFUSED = "refused"
    REJECTED = "rejected"
    RESERVE_ADJUSTMENT = "reserveAdjustment"
    RESERVE_ADJUSTMENT_PENDING = "reserveAdjustmentPending"
    RETURNED = "returned"
    REVERSED = "reversed"
    SECOND_CHARGEBACK = "secondChargeback"
    SECOND_CHARGEBACK_PENDING = "secondChargebackPending"
    UNDEFINED = "undefined"

    __str__ = str.__str__


Status51OrStr: TypeAlias = Annotated[Status51 | str, open_enum_validator(Status51)]
