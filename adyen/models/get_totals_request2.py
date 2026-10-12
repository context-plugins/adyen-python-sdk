from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.total_detail import TotalDetailOrStr
from .total_filter2 import TotalFilter2, TotalFilter2Dict


class GetTotalsRequest2(SdkBaseModel):
    """Content of the Get Totals Request message."""

    total_details: Optional[list[TotalDetailOrStr]] = Field(default=UNSET, alias="TotalDetails")
    """Indicates the hierarchical structure of the reconciliation result of the Sale to POI reconciliation. Required to
    present totals per value of element included in this cluster (POI Terminal, Sale Terminal, Cashier, Shift,
    TotalsGroupID). Possible values:
    * **OperatorID**
    * **POIID**
    * **SaleID**
    * **ShiftNumber**
    * **TotalsGroupID**"""

    total_filter: Optional[TotalFilter2] = Field(default=UNSET, alias="TotalFilter")
    """Filter to compute the totals. Used for the Get Totals, to request totals for a (or a combination of) particular
    value of the POI Terminal, Sale Terminal, Cashier, Shift, or TotalsGroupID."""


class GetTotalsRequest2Dict(TypedDict):
    total_details: NotRequired[list[TotalDetailOrStr]]
    total_filter: NotRequired[TotalFilter2Dict]
