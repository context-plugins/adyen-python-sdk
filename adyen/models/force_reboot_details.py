from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.type210 import Type210, Type210OrStr


class ForceRebootDetails(SdkBaseModel):
    type_: Type210OrStr = Field(default=Type210.FORCE_REBOOT, alias="type")
    """The type of terminal action. The value **ForceReboot** triggers an immediate reboot of the specified
    terminal(s)."""


class ForceRebootDetailsDict(TypedDict):
    type_: NotRequired[Type210OrStr]
