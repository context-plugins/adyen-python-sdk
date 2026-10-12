from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .network_token2 import NetworkToken2, NetworkToken2Dict


class GetNetworkTokenResponse(SdkBaseModel):
    token: NetworkToken2
    """The details of the network token."""


class GetNetworkTokenResponseDict(TypedDict):
    token: NetworkToken2Dict
