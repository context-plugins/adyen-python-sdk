from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .href1 import Href1, Href1Dict
from .href6 import Href6, Href6Dict


class Links4(SdkBaseModel):
    cancel: Optional[Href6] = UNSET
    """The URL to where the user must be redirected after a payment has been canceled."""

    success: Optional[Href1] = UNSET
    """The URL to where the user must be redirected after a successful payment."""


class Links4Dict(TypedDict):
    cancel: NotRequired[Href6 | Href6Dict]
    success: NotRequired[Href1 | Href1Dict]
