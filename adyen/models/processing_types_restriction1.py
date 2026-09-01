from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value4 import Value4OrStr


class ProcessingTypesRestriction1(SdkBaseModel):
    """List of processing types and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value4OrStr]] = UNSET
    """List of processing types.

    Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**."""


class ProcessingTypesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[Value4OrStr]]
