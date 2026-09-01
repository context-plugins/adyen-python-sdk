from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleTerminalData(SdkBaseModel):
    """Information related to the software and hardware features of the Sale Terminal. Sent in the Login Request if a
    Sale Terminal is involved in the login. In other messages, sent when a logical device is out of order
    (SaleCapabilities) or when other data have changed or were missing in the Login."""

    totals_group_id: Optional[str] = Field(default=UNSET, alias="TotalsGroupID")
    """Identification of a group of transactions on a POI Terminal, having the same Sale features. Could be used to
    group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login
    Request."""


class SaleTerminalDataDict(TypedDict):
    totals_group_id: NotRequired[str]
