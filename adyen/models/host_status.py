from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HostStatus(SdkBaseModel):
    """Indicate the reachability of the host by the POI Terminal. State of a Host."""

    acquirer_id: int = Field(alias="AcquirerID")
    """Identification of the Acquirer."""

    is_reachable_flag: Optional[bool] = Field(default=UNSET, alias="IsReachableFlag")
    """Indicate if a Host is reachable."""


class HostStatusDict(TypedDict):
    acquirer_id: int
    is_reachable_flag: NotRequired[bool]
