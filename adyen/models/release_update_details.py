from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type61 import Type61, Type61OrStr


class ReleaseUpdateDetails(SdkBaseModel):
    type_: Type61OrStr = Field(default=Type61.RELEASE_UPDATE, alias="type")
    """Type of terminal action: Update Release."""

    update_at_first_maintenance_call: Optional[bool] = Field(default=UNSET, alias="updateAtFirstMaintenanceCall")
    """Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will
    update on its configured reboot time."""


class ReleaseUpdateDetailsDict(TypedDict):
    type_: NotRequired[Type61OrStr]
    update_at_first_maintenance_call: NotRequired[bool]
