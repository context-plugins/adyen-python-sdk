from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.global_status1 import GlobalStatus1OrStr
from .enums.printer_status1 import PrinterStatus1OrStr


class Poistatus1(SdkBaseModel):
    """State of a POI Terminal. If ``Response.Result`` is Success."""

    global_status: GlobalStatus1OrStr = Field(alias="GlobalStatus")
    """Global status of a POI Server or POI Terminal. Possible values:
    * **Busy**
    * **Maintenance**
    * **OK**
    * **Unreachable**"""

    security_ok_flag: Optional[bool] = Field(default=UNSET, alias="SecurityOKFlag")
    """Indicates if the security module of the POI is working and usable. If security module present."""

    pedok_flag: Optional[bool] = Field(default=UNSET, alias="PEDOKFlag")
    """Indicates if the PED is working and usable. If PED present."""

    card_reader_ok_flag: Optional[bool] = Field(default=UNSET, alias="CardReaderOKFlag")
    """Indicates if the card readers are working and usable. If card reader device present."""

    printer_status: Optional[PrinterStatus1OrStr] = Field(default=UNSET, alias="PrinterStatus")
    """Possible values:
    * **NoPaper**
    * **OK**
    * **OutOfOrder**
    * **PaperJam**
    * **PaperLow**"""

    communication_ok_flag: Optional[bool] = Field(default=UNSET, alias="CommunicationOKFlag")
    """Indicates if the communication infrastructure is working and usable. If communication infrastructure present."""

    fraud_prevention_flag: Optional[bool] = Field(default=UNSET, alias="FraudPreventionFlag")
    """Indicates a suspicion of fraud by the POI System. Could be set to True by the POI system to notify to the Sale
    system and the Cashier that a suspicion of fraud had been detected on the POI as an unexpected reboot of the POI."""


class Poistatus1Dict(TypedDict):
    global_status: GlobalStatus1OrStr
    security_ok_flag: NotRequired[bool]
    pedok_flag: NotRequired[bool]
    card_reader_ok_flag: NotRequired[bool]
    printer_status: NotRequired[PrinterStatus1OrStr]
    communication_ok_flag: NotRequired[bool]
    fraud_prevention_flag: NotRequired[bool]
