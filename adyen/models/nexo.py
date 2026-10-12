from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event_url2 import EventUrl2, EventUrl2Dict
from .key1 import Key1, Key1Dict
from .notification2 import Notification2, Notification2Dict
from .notification_url2 import NotificationUrl2, NotificationUrl2Dict


class Nexo(SdkBaseModel):
    display_urls: Optional[NotificationUrl2] = Field(default=UNSET, alias="displayUrls")
    """The list of local and public URLs to send display notifications to when using Terminal API."""

    encryption_key: Optional[Key1] = Field(default=UNSET, alias="encryptionKey")
    """The key you share with Adyen to secure local communications when using Terminal API."""

    event_urls: Optional[EventUrl2] = Field(default=UNSET, alias="eventUrls")
    """The list of local and public URLs to send event notifications to when using Terminal API."""

    nexo_event_urls: Optional[list[str]] = Field(default=UNSET, alias="nexoEventUrls")
    """One or more URLs to send event messages to when using Terminal API."""

    notification: Optional[Notification2] = UNSET
    """Configures sending event notifications by pressing a button on a terminal, for example used for pay-at-table."""


class NexoDict(TypedDict):
    display_urls: NotRequired[NotificationUrl2Dict]
    encryption_key: NotRequired[Key1Dict]
    event_urls: NotRequired[EventUrl2Dict]
    nexo_event_urls: NotRequired[list[str]]
    notification: NotRequired[Notification2Dict]
