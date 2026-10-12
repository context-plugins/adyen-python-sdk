from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_action_schedule_detail import TerminalActionScheduleDetail, TerminalActionScheduleDetailDict
from .unions.action_details import ActionDetails, ActionDetailsDict


class ScheduleTerminalActionsResponse(SdkBaseModel):
    action_details: Optional[ActionDetails] = Field(default=UNSET, alias="actionDetails")
    """Information about the action to take."""

    items: Optional[list[TerminalActionScheduleDetail]] = UNSET
    """A list containing a terminal ID and an action ID for each terminal that the action was scheduled for."""

    scheduled_at: Optional[str] = Field(default=UNSET, alias="scheduledAt")
    """The date and time when the action should happen. Format: `RFC 3339 <https://www.rfc-editor.org/rfc/rfc3339>`__,
    but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+0100** The action is sent with the
    first `maintenance call
    <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api#when-actions-take-effect>`__
    after the specified date and time in the time zone of the terminal. An empty value causes the action to be sent as
    soon as possible: at the next maintenance call."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The unique ID of the `store <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores>`__. If
    present, all terminals in the ``terminalIds`` list must be assigned to this store."""

    terminals_with_errors: Optional[dict[str, Any]] = Field(default=UNSET, alias="terminalsWithErrors")
    """The validation errors that occurred in the list of terminals, and for each error the IDs of the terminals that
    the error applies to."""

    total_errors: Optional[int] = Field(default=UNSET, alias="totalErrors")
    """The number of terminals for which scheduling the action failed."""

    total_scheduled: Optional[int] = Field(default=UNSET, alias="totalScheduled")
    """The number of terminals for which the action was successfully scheduled. This doesn't mean the action has
    happened yet."""


class ScheduleTerminalActionsResponseDict(TypedDict):
    action_details: NotRequired[ActionDetailsDict]
    items: NotRequired[list[TerminalActionScheduleDetailDict]]
    scheduled_at: NotRequired[str]
    store_id: NotRequired[str]
    terminals_with_errors: NotRequired[dict[str, Any]]
    total_errors: NotRequired[int]
    total_scheduled: NotRequired[int]
