from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisableResult(SdkBaseModel):
    response: Optional[str] = UNSET
    """Depending on whether a specific recurring detail was in the request, result is either
    [detail-successfully-disabled] or [all-details-successfully-disabled]."""


class DisableResultDict(TypedDict):
    response: NotRequired[str]
