from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalConnectivityEthernet(SdkBaseModel):
    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The terminal's ethernet IP address."""

    link_negotiation: Optional[str] = Field(default=UNSET, alias="linkNegotiation")
    """The ethernet link negotiation that the terminal uses."""

    mac_address: Optional[str] = Field(default=UNSET, alias="macAddress")
    """The terminal's ethernet MAC address."""


class TerminalConnectivityEthernetDict(TypedDict):
    ip_address: NotRequired[str]
    link_negotiation: NotRequired[str]
    mac_address: NotRequired[str]
