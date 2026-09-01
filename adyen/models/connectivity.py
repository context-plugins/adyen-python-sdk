from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.simcard_status import SimcardStatusOrStr
from .event_url3 import EventUrl3, EventUrl3Dict


class Connectivity(SdkBaseModel):
    simcard_status: Optional[SimcardStatusOrStr] = Field(default=UNSET, alias="simcardStatus")
    """Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level,
    and only for models that support cellular connectivity.

    Possible values:
    * **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal
        itself, in the **Network** settings.
    * **INVENTORY**: the SIM card is not activated. The terminal can't use cellular connectivity."""

    terminal_ip_address_url: Optional[EventUrl3] = Field(default=UNSET, alias="terminalIPAddressURL")
    """The list of local and public URLs to send notifications to when using local integrations."""


class ConnectivityDict(TypedDict):
    simcard_status: NotRequired[SimcardStatusOrStr]
    terminal_ip_address_url: NotRequired[EventUrl3 | EventUrl3Dict]
