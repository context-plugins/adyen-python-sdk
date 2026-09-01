from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalActionScheduleDetail(SdkBaseModel):
    id: Optional[str] = UNSET
    """The ID of the action on the specified terminal."""

    terminal_id: Optional[str] = Field(default=UNSET, alias="terminalId")
    """The unique ID of the terminal that the action applies to."""


class TerminalActionScheduleDetailDict(TypedDict):
    id: NotRequired[str]
    terminal_id: NotRequired[str]
