from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .network_token import NetworkToken, NetworkTokenDict


class ListNetworkTokensResponse(SdkBaseModel):
    network_tokens: Optional[list[NetworkToken]] = Field(default=UNSET, alias="networkTokens")
    """List of network tokens."""


class ListNetworkTokensResponseDict(TypedDict):
    network_tokens: NotRequired[list[NetworkToken | NetworkTokenDict]]
