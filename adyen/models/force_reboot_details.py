from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type210 import Type210OrStr


class ForceRebootDetails(SdkBaseModel):
    type_: Optional[Type210OrStr] = Field(default=UNSET, alias="type")
    """The type of terminal action. The value **ForceReboot** triggers an immediate reboot of the specified
    terminal(s)."""


class ForceRebootDetailsDict(TypedDict):
    type_: NotRequired[Type210OrStr]
