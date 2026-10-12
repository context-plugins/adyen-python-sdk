from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_rule1 import TransactionRule1, TransactionRule1Dict


class TransactionRuleResponse(SdkBaseModel):
    transaction_rule: Optional[TransactionRule1] = Field(default=UNSET, alias="transactionRule")
    """The transaction rule."""


class TransactionRuleResponseDict(TypedDict):
    transaction_rule: NotRequired[TransactionRule1Dict]
