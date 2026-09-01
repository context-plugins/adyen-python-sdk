from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageCategory2(str, Enum):
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

    ABORT = "Abort"
    ADMIN = "Admin"
    BALANCE_INQUIRY = "BalanceInquiry"
    CARD_ACQUISITION = "CardAcquisition"
    DIAGNOSIS = "Diagnosis"
    DISPLAY = "Display"
    ENABLE_SERVICE = "EnableService"
    EVENT = "Event"
    GET_TOTALS = "GetTotals"
    INPUT = "Input"
    INPUT_UPDATE = "InputUpdate"
    LOGIN = "Login"
    LOGOUT = "Logout"
    LOYALTY = "Loyalty"
    PAYMENT = "Payment"
    PRINT = "Print"
    RECONCILIATION = "Reconciliation"
    REVERSAL = "Reversal"
    STORED_VALUE = "StoredValue"
    TRANSACTION_STATUS = "TransactionStatus"
    NONE = "None"

    __str__ = str.__str__


MessageCategory2OrStr: TypeAlias = Annotated[MessageCategory2 | str, open_enum_validator(MessageCategory2)]
