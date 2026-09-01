from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value5 import Value5OrStr


class SourceAccountTypesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value5OrStr]] = UNSET
    """The list of source account types to be evaluated."""


class SourceAccountTypesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[Value5OrStr]]
