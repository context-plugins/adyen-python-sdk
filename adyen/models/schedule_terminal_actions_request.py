from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.action_details import ActionDetails, ActionDetailsDict


class ScheduleTerminalActionsRequest(SdkBaseModel):
    action_details: Optional[ActionDetails] = Field(default=UNSET, alias="actionDetails")
    """Information about the action to take."""

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

    terminal_ids: Optional[list[str]] = Field(default=UNSET, alias="terminalIds")
    """A list of unique IDs of the terminals to apply the action to. You can extract the IDs from the
    https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminals response. Maximum length: 100 IDs."""


class ScheduleTerminalActionsRequestDict(TypedDict):
    action_details: NotRequired[ActionDetails | ActionDetailsDict]
    scheduled_at: NotRequired[str]
    store_id: NotRequired[str]
    terminal_ids: NotRequired[list[str]]
