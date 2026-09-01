from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value5 import Value5OrStr


class SourceAccountTypesRestriction1(SdkBaseModel):
    """Contains a list of source account types and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **balanceAccount**
    - **businessAccount**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value5OrStr]] = UNSET
    """The list of source account types to be evaluated."""


class SourceAccountTypesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[Value5OrStr]]
