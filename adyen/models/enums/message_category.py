from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageCategory(str, Enum):
    """Possible values:
    * **Abort**
    * **Admin**
    * **BalanceInquiry**
    * **CardAcquisition**
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
    * **Payment**
    * **Print**
    * **Reconciliation**
    * **Reversal**
    * **StoredValue**
    * **TransactionStatus**
    * **None**"""

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


MessageCategoryOrStr: TypeAlias = Annotated[MessageCategory | str, open_enum_validator(MessageCategory)]
