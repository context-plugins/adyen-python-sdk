from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.message_category1 import MessageCategory1OrStr
from .enums.message_class1 import MessageClass1OrStr
from .enums.message_type1 import MessageType1OrStr


class MessageHeader(SdkBaseModel):
    """Message header of the Sale to POI protocol message. It conveys Information related to the Sale to POI protocol
    management."""

    protocol_version: Optional[str] = Field(default=UNSET, alias="ProtocolVersion")
    """If MessageCategory is Login or Diagnosis."""

    message_class: MessageClass1OrStr = Field(alias="MessageClass")
    """Class of the message. Possible values:
    * **Device**
    * **Event**
    * **Service**"""

    message_category: MessageCategory1OrStr = Field(alias="MessageCategory")
    """Category of message. Possible values:
    * **Abort**
    * **Admin**
    * **BalanceInquiry**
    * **Batch**
    * **CardAcquisition**
    * **CardReaderInit**
    * **CardReaderPowerOff**
    * **Diagnosis**
    * **Display**
    * **EnableService**
    * **Event**
    * **GetTotals**
    * **Input**
    * **InputUpdate**
    * **Login**
    * **Logout**
    * **Loyalty**
    * **None**
    * **PIN**
    * **Payment**
    * **Print**
    * **Reconciliation**
    * **Reversal**
    * **Sound**
    * **StoredValue**
    * **TransactionStatus**
    * **Transmit**"""

    message_type: MessageType1OrStr = Field(alias="MessageType")
    """Type of message of the Sale to POI protocol. Possible values:
    * **Notification**
    * **Request**
    * **Response**"""

    service_id: Optional[str] = Field(default=UNSET, alias="ServiceID")
    """Identification of a message pair, which processes a transaction. Required if Service or Event MessageClass
    message or if Device MessageClass and request from POI or response from Sale."""

    device_id: Optional[str] = Field(default=UNSET, alias="DeviceID")
    """Identification of a device message pair. If Device MessageClass."""

    sale_id: str = Field(alias="SaleID")
    """Identification of a Sale System or a Sale Terminal for the Sale to POI protocol."""

    poiid: str = Field(alias="POIID")
    """Identification of a POI System or a POI Terminal for the Sale to POI protocol."""


class MessageHeaderDict(TypedDict):
    protocol_version: NotRequired[str]
    message_class: MessageClass1OrStr
    message_category: MessageCategory1OrStr
    message_type: MessageType1OrStr
    service_id: NotRequired[str]
    device_id: NotRequired[str]
    sale_id: str
    poiid: str
