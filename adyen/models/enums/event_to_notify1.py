from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EventToNotify1(str, Enum):
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

    BEGIN_MAINTENANCE = "BeginMaintenance"
    END_MAINTENANCE = "EndMaintenance"
    SHUTDOWN = "Shutdown"
    INITIALISED = "Initialised"
    OUT_OF_ORDER = "OutOfOrder"
    COMPLETED = "Completed"
    ABORT = "Abort"
    SALE_WAKE_UP = "SaleWakeUp"
    SALE_ADMIN = "SaleAdmin"
    CUSTOMER_LANGUAGE = "CustomerLanguage"
    KEY_PRESSED = "KeyPressed"
    SECURITY_ALARM = "SecurityAlarm"
    STOP_ASSISTANCE = "StopAssistance"
    CARD_INSERTED = "CardInserted"
    CARD_REMOVED = "CardRemoved"
    REJECT = "Reject"
    USE_ANOTHER_CARD_FOR_PREAUTH = "UseAnotherCardForPreauth"
    SCAN_BARCODE_RESULT = "ScanBarcodeResult"

    __str__ = str.__str__


EventToNotify1OrStr: TypeAlias = Annotated[EventToNotify1 | str, open_enum_validator(EventToNotify1)]
