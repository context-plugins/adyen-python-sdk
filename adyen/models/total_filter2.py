from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalFilter2(SdkBaseModel):
    """Filter to compute the totals. Used for the Get Totals, to request totals for a (or a combination of) particular
    value of the POI Terminal, Sale Terminal, Cashier, Shift, or TotalsGroupID."""

    poiid: Optional[str] = Field(default=UNSET, alias="POIID")
    """Identification of a POI System or a POI Terminal for the Sale to POI protocol."""

    sale_id: Optional[str] = Field(default=UNSET, alias="SaleID")
    """Identification of a Sale System or a Sale Terminal for the Sale to POI protocol."""

    operator_id: Optional[str] = Field(default=UNSET, alias="OperatorID")
    """Identification of the Cashier or Operator."""

    shift_number: Optional[str] = Field(default=UNSET, alias="ShiftNumber")
    """Shift number."""

    totals_group_id: Optional[str] = Field(default=UNSET, alias="TotalsGroupID")
    """Sent if totals in the response have to be computed only for this particular value of TotalsGroupID."""


class TotalFilter2Dict(TypedDict):
    poiid: NotRequired[str]
    sale_id: NotRequired[str]
    operator_id: NotRequired[str]
    shift_number: NotRequired[str]
    totals_group_id: NotRequired[str]
