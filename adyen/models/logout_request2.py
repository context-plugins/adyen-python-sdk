from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LogoutRequest2(SdkBaseModel):
    """Content of the Logout Request message."""

    maintenance_allowed: Optional[bool] = Field(default=UNSET, alias="MaintenanceAllowed")
    """Indicates that the POI terminal is able to or has to go to maintenance. Sent in the Logout Request to express
    that after closing the session, the POI may go to maintenance."""


class LogoutRequest2Dict(TypedDict):
    maintenance_allowed: NotRequired[bool]
