from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .display_output import DisplayOutput, DisplayOutputDict
from .enums.event_to_notify1 import EventToNotify1OrStr


class EventNotification2(SdkBaseModel):
    """Content of the EventNotification message."""

    time_stamp: RFC3339DateTime = Field(alias="TimeStamp")
    """Date and time of a transaction for the Sale System, the POI System or the Acquirer."""

    event_to_notify: EventToNotify1OrStr = Field(alias="EventToNotify")
    """Event the POI notifies to the Sale System. Possible values:
    * **Abort**
    * **BeginMaintenance**
    * **CardInserted**
    * **CardRemoved**
    * **Completed**
    * **CustomerLanguage**
    * **EndMaintenance**
    * **Initialised**
    * **KeyPressed**
    * **OutOfOrder**
    * **Reject**
    * **SaleAdmin**
    * **SaleWakeUp**
    * **ScanBarcodeResult**
    * **SecurityAlarm**
    * **Shutdown**
    * **StopAssistance**
    * **UseAnotherCardForPreauth**"""

    event_details: Optional[str] = Field(default=UNSET, alias="EventDetails")
    """Information about the event the POI notifies to the Sale System. If present, the Sale logs it for further
    examination."""

    rejected_message: Optional[str] = Field(default=UNSET, alias="RejectedMessage")
    """Message request rejected by the receiver. Mandatory if EventToNotify is Reject, absent in other cases."""

    maintenance_required_flag: bool = Field(default=False, alias="MaintenanceRequiredFlag")
    """Indicates if the occurred event requires maintenance call or action."""

    display_output: Optional[list[DisplayOutput]] = Field(default=UNSET, alias="DisplayOutput")
    """Information to display and the way to process the display. To display an event message."""


class EventNotification2Dict(TypedDict):
    time_stamp: RFC3339DateTime
    event_to_notify: EventToNotify1OrStr
    event_details: NotRequired[str]
    rejected_message: NotRequired[str]
    maintenance_required_flag: NotRequired[bool]
    display_output: NotRequired[list[DisplayOutputDict]]
