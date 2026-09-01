from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.result2 import Result2OrStr


class SubjectErasureResponse(SdkBaseModel):
    result: Optional[Result2OrStr] = UNSET
    """The result of this operation."""


class SubjectErasureResponseDict(TypedDict):
    result: NotRequired[Result2OrStr]
