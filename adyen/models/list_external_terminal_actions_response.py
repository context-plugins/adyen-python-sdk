from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .external_terminal_action import ExternalTerminalAction, ExternalTerminalActionDict


class ListExternalTerminalActionsResponse(SdkBaseModel):
    data: Optional[list[ExternalTerminalAction]] = UNSET
    """The list of terminal actions."""


class ListExternalTerminalActionsResponseDict(TypedDict):
    data: NotRequired[list[ExternalTerminalActionDict]]
