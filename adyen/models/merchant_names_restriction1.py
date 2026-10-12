from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .string_match import StringMatch, StringMatchDict


class MerchantNamesRestriction1(SdkBaseModel):
    """List of names that will be compared to the merchant name according to the matching type.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[StringMatch]] = UNSET


class MerchantNamesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[StringMatchDict]]
