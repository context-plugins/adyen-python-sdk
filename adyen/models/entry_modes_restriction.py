from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value2 import Value2OrStr


class EntryModesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value2OrStr]] = UNSET
    """List of point-of-sale entry modes.

    Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**."""


class EntryModesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[Value2OrStr]]
