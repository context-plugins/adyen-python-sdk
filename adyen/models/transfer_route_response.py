from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_route import TransferRoute, TransferRouteDict


class TransferRouteResponse(SdkBaseModel):
    transfer_routes: Optional[list[TransferRoute]] = Field(default=UNSET, alias="transferRoutes")
    """List of available priorities for a transfer, along with requirements. Use this information to initiate a
    transfer."""


class TransferRouteResponseDict(TypedDict):
    transfer_routes: NotRequired[list[TransferRouteDict]]
