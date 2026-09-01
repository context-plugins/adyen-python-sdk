from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleTerminalData2(SdkBaseModel):
    """Information related to the software and hardware feature of the Sale Terminal. Present if the login involve a
    Sale Terminal."""

    totals_group_id: Optional[str] = Field(default=UNSET, alias="TotalsGroupID")
    """Identification of a group of transactions on a POI Terminal, having the same Sale features. Could be used to
    group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login
    Request."""


class SaleTerminalData2Dict(TypedDict):
    totals_group_id: NotRequired[str]
