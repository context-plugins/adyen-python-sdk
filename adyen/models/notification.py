from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.category import CategoryOrStr


class Notification(SdkBaseModel):
    category: Optional[CategoryOrStr] = UNSET
    """The type of event notification sent when you select the notification button."""

    details: Optional[str] = UNSET
    """The text shown in the prompt which opens when you select the notification button. For example, the description of
    the input box for pay-at-table."""

    enabled: Optional[bool] = UNSET
    """Enables sending event notifications either by pressing the Confirm key on terminals with a keypad or by tapping
    the event notification button on the terminal screen."""

    show_button: Optional[bool] = Field(default=UNSET, alias="showButton")
    """Shows or hides the event notification button on the screen of terminal models that have a keypad."""

    title: Optional[str] = UNSET
    """The name of the notification button on the terminal screen."""


class NotificationDict(TypedDict):
    category: NotRequired[CategoryOrStr]
    details: NotRequired[str]
    enabled: NotRequired[bool]
    show_button: NotRequired[bool]
    title: NotRequired[str]
