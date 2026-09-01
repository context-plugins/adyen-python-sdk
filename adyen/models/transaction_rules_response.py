from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_rule import TransactionRule, TransactionRuleDict


class TransactionRulesResponse(SdkBaseModel):
    transaction_rules: Optional[list[TransactionRule]] = Field(default=UNSET, alias="transactionRules")
    """List of transaction rules."""


class TransactionRulesResponseDict(TypedDict):
    transaction_rules: NotRequired[list[TransactionRule | TransactionRuleDict]]
