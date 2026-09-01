from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TokenRequestorsRestriction1(SdkBaseModel):
    """List of token requestor IDs and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[str]] = UNSET


class TokenRequestorsRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[str]]
