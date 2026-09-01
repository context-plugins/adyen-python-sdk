from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MccsRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[str]] = UNSET
    """List of merchant category codes (MCCs)."""


class MccsRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[str]]
