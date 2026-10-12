from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allowed_origin import AllowedOrigin, AllowedOriginDict


class AllowedOriginsResponse(SdkBaseModel):
    data: Optional[list[AllowedOrigin]] = UNSET
    """List of allowed origins."""


class AllowedOriginsResponseDict(TypedDict):
    data: NotRequired[list[AllowedOriginDict]]
