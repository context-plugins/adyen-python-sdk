from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InternationalTransactionRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[bool] = UNSET
    """Boolean indicating whether transaction is an international transaction.

    Possible values:

    - **true**: The transaction is an international transaction.

    - **false**: The transaction is a domestic transaction."""


class InternationalTransactionRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[bool]
