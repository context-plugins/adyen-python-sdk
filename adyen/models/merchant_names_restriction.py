from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .string_match import StringMatch, StringMatchDict


class MerchantNamesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[StringMatch]] = UNSET


class MerchantNamesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[StringMatchDict]]
