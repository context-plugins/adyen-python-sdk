from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionRuleReference2(SdkBaseModel):
    """Contains information about the transaction rule."""

    description: Optional[str] = UNSET
    """The description of the resource."""

    id: Optional[str] = UNSET
    """The unique identifier of the resource."""

    outcome_type: Optional[str] = Field(default=UNSET, alias="outcomeType")
    """The outcome type of the rule."""

    reference: Optional[str] = UNSET
    """The reference for the resource."""

    score: Optional[int] = UNSET
    """The transaction score determined by the rule. Returned only when ``outcomeType`` is **scoreBased**."""


class TransactionRuleReference2Dict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    outcome_type: NotRequired[str]
    reference: NotRequired[str]
    score: NotRequired[int]
