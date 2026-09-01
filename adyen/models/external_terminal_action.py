from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ExternalTerminalAction(SdkBaseModel):
    action_type: Optional[str] = Field(default=UNSET, alias="actionType")
    """The type of terminal action: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, or
    **UninstallAndroidCertificate**."""

    config: Optional[str] = UNSET
    """Technical information about the terminal action."""

    confirmed_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="confirmedAt")
    """The date and time when the action was carried out."""

    id: Optional[str] = UNSET
    """The unique ID of the terminal action."""

    result: Optional[str] = UNSET
    """The result message for the action."""

    scheduled_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="scheduledAt")
    """The date and time when the action was scheduled to happen."""

    status: Optional[str] = UNSET
    """The status of the terminal action: **pending**, **successful**, **failed**, **cancelled**, or **tryLater**."""

    terminal_id: Optional[str] = Field(default=UNSET, alias="terminalId")
    """The unique ID of the terminal that the action applies to."""


class ExternalTerminalActionDict(TypedDict):
    action_type: NotRequired[str]
    config: NotRequired[str]
    confirmed_at: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    result: NotRequired[str]
    scheduled_at: NotRequired[RFC3339DateTime]
    status: NotRequired[str]
    terminal_id: NotRequired[str]
