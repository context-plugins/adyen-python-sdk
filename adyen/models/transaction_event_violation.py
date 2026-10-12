from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_rule_reference2 import TransactionRuleReference2, TransactionRuleReference2Dict
from .transaction_rule_source2 import TransactionRuleSource2, TransactionRuleSource2Dict


class TransactionEventViolation(SdkBaseModel):
    reason: Optional[str] = UNSET
    """An explanation about why the transaction rule failed."""

    transaction_rule: Optional[TransactionRuleReference2] = Field(default=UNSET, alias="transactionRule")
    """Contains information about the transaction rule."""

    transaction_rule_source: Optional[TransactionRuleSource2] = Field(default=UNSET, alias="transactionRuleSource")
    """Contains information about the resource to which the transaction rule applies."""


class TransactionEventViolationDict(TypedDict):
    reason: NotRequired[str]
    transaction_rule: NotRequired[TransactionRuleReference2Dict]
    transaction_rule_source: NotRequired[TransactionRuleSource2Dict]
