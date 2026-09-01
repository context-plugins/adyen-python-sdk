from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MccsRestriction1(SdkBaseModel):
    """List of merchant category codes (MCCs) and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[str]] = UNSET
    """List of merchant category codes (MCCs)."""


class MccsRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[str]]
