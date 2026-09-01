from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.result1 import Result1OrStr


class ValidateShopperIdResponse(SdkBaseModel):
    reason: Optional[str] = UNSET
    """Reason for the result."""

    result: Optional[Result1OrStr] = UNSET
    """Result of the validation. Ex: valid, invalid, unknown"""


class ValidateShopperIdResponseDict(TypedDict):
    reason: NotRequired[str]
    result: NotRequired[Result1OrStr]
