from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorCondition1(str, Enum):
    """Condition that has produced an error on the processing of a message request. Returned if Result is not Success.
    Possible values:
    * **Aborted**
    * **Busy**
    * **Cancel**
    * **DeviceOut**
    * **InProgress**
    * **InsertedCard**
    * **InvalidCard**
    * **LoggedOut**
    * **MessageFormat**
    * **NotAllowed**
    * **NotFound**
    * **PaymentRestriction**
    * **Refusal**
    * **UnavailableDevice**
    * **UnavailableService**
    * **UnreachableHost**
    * **WrongPIN**"""

    ABORTED = "Aborted"
    BUSY = "Busy"
    CANCEL = "Cancel"
    DEVICE_OUT = "DeviceOut"
    INSERTED_CARD = "InsertedCard"
    IN_PROGRESS = "InProgress"
    LOGGED_OUT = "LoggedOut"
    MESSAGE_FORMAT = "MessageFormat"
    NOT_ALLOWED = "NotAllowed"
    NOT_FOUND = "NotFound"
    PAYMENT_RESTRICTION = "PaymentRestriction"
    REFUSAL = "Refusal"
    UNAVAILABLE_DEVICE = "UnavailableDevice"
    UNAVAILABLE_SERVICE = "UnavailableService"
    INVALID_CARD = "InvalidCard"
    UNREACHABLE_HOST = "UnreachableHost"
    WRONG_PIN = "WrongPIN"

    __str__ = str.__str__


ErrorCondition1OrStr: TypeAlias = Annotated[ErrorCondition1 | str, open_enum_validator(ErrorCondition1)]
