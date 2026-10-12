from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_event_violation import TransactionEventViolation, TransactionEventViolationDict


class TransactionRulesResult(SdkBaseModel):
    advice: Optional[str] = UNSET
    """The advice given by the Risk analysis."""

    all_hard_block_rules_passed: Optional[bool] = Field(default=UNSET, alias="allHardBlockRulesPassed")
    """Indicates whether the transaction passed the evaluation for all hardblock rules"""

    score: Optional[int] = UNSET
    """The score of the Risk analysis."""

    triggered_transaction_rules: Optional[list[TransactionEventViolation]] = Field(
        default=UNSET, alias="triggeredTransactionRules"
    )
    """Array containing all the transaction rules that the transaction triggered."""


class TransactionRulesResultDict(TypedDict):
    advice: NotRequired[str]
    all_hard_block_rules_passed: NotRequired[bool]
    score: NotRequired[int]
    triggered_transaction_rules: NotRequired[list[TransactionEventViolationDict]]
