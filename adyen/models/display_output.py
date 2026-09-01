from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.device11 import Device11OrStr
from .enums.info_qualify1 import InfoQualify1OrStr
from .menu_entry import MenuEntry, MenuEntryDict
from .output_content1 import OutputContent1, OutputContent1Dict


class DisplayOutput(SdkBaseModel):
    """Information to display and how to process it. Contains a complete display operation for a Display or an Input
    Device type. For the Input Devices, Diagnosis and ``EnableService``, ``ResponseRequiredFlag``, and
    ``MinimumDisplayTime`` shall be absent."""

    response_required_flag: Optional[bool] = Field(default=UNSET, alias="ResponseRequiredFlag")
    """Indicates if the message response is required."""

    minimum_display_time: Optional[int] = Field(default=UNSET, alias="MinimumDisplayTime")
    """Number of seconds the message has to be displayed."""

    device: Device11OrStr = Field(alias="Device")
    """Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display,
    print, or store), or input (keyboard) for the Cashier or the Customer. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    info_qualify: InfoQualify1OrStr = Field(alias="InfoQualify")
    """Qualification of the information to sent to an output logical device, to display or print to the Cashier or the
    Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical
    device or to present the information accordingly. Possible values:
    * **CustomerAssistance**
    * **Display**
    * **Document**
    * **Error**
    * **Input**
    * **POIReplication**
    * **Receipt**
    * **Sound**
    * **Status**
    * **Voucher**"""

    output_content: OutputContent1 = Field(alias="OutputContent")
    """Content to display or print."""

    menu_entry: Optional[list[MenuEntry]] = Field(default=UNSET, alias="MenuEntry")
    """An entry of the menu to present to the Cashier. It conveys the message text and parameters of the menu entry.
    This output data could be only provided for an input command, in order to choose an entryof the menu."""

    output_signature: Optional[str] = Field(default=UNSET, alias="OutputSignature")
    """Vendor-specific signature of the text message to display or print. If protection has to be provided to the vendor
    on the text to display or print."""


class DisplayOutputDict(TypedDict):
    response_required_flag: NotRequired[bool]
    minimum_display_time: NotRequired[int]
    device: Device11OrStr
    info_qualify: InfoQualify1OrStr
    output_content: OutputContent1 | OutputContent1Dict
    menu_entry: NotRequired[list[MenuEntry | MenuEntryDict]]
    output_signature: NotRequired[str]
