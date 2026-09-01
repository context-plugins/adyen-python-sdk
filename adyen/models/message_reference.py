from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.message_category2 import MessageCategory2OrStr


class MessageReference(SdkBaseModel):
    """Identification of a previous POI transaction. To abort a transaction in progress or to request the status of a
    transaction from which no response has been received. It identifies the message header of the message request to
    abort or request the status."""

    message_category: Optional[MessageCategory2OrStr] = Field(default=UNSET, alias="MessageCategory")
    """Category of message. CardAcquisition, Display, Input, Loyalty, Payment, Print, CardReaderInit,
    CardReaderPowerOff. Possible values:
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

    service_id: Optional[str] = Field(default=UNSET, alias="ServiceID")
    """Identification of a message pair, which processes a transaction."""

    device_id: Optional[str] = Field(default=UNSET, alias="DeviceID")
    """Identification of a device message pair."""

    sale_id: Optional[str] = Field(default=UNSET, alias="SaleID")
    """Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. default MessageHeader.SaleID."""

    poiid: Optional[str] = Field(default=UNSET, alias="POIID")
    """Identification of a POI System or a POI Terminal for the Sale to POI protocol. Default
    ``MessageHeader.POIID``."""


class MessageReferenceDict(TypedDict):
    message_category: NotRequired[MessageCategory2OrStr]
    service_id: NotRequired[str]
    device_id: NotRequired[str]
    sale_id: NotRequired[str]
    poiid: NotRequired[str]
