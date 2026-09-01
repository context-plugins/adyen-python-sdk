from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status31 import Status31OrStr


class TerminalConnectivityCellular(SdkBaseModel):
    iccid: Optional[str] = UNSET
    """The integrated circuit card identifier (ICCID) of the primary SIM card in the terminal."""

    iccid2: Optional[str] = UNSET
    """The integrated circuit card identifier (ICCID) of the secondary SIM card in the terminal, typically used for a
    `third-party SIM card
    <https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/#using-a-third-party-sim-card>`__."""

    status: Optional[Status31OrStr] = UNSET
    """On a terminal that supports 3G or 4G connectivity, indicates the status of the primary SIM card in the
    terminal."""


class TerminalConnectivityCellularDict(TypedDict):
    iccid: NotRequired[str]
    iccid2: NotRequired[str]
    status: NotRequired[Status31OrStr]
