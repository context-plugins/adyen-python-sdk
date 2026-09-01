from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExternalReason2(SdkBaseModel):
    """The external reason of this transfer."""

    code: Optional[str] = UNSET
    """The reason code."""

    description: Optional[str] = UNSET
    """The description of the reason code."""

    namespace: Optional[str] = UNSET
    """The namespace for the reason code."""


class ExternalReason2Dict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    namespace: NotRequired[str]
