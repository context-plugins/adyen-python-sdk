from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SameAmountRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[bool] = UNSET


class SameAmountRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[bool]
