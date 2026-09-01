from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorCondition(str, Enum):
    """Possible values:
    * **Aborted**
    * **Busy**
    * **Cancel**
    * **DeviceOut**
    * **InsertedCard**
    * **InProgress**
    * **LoggedOut**
    * **MessageFormat**
    * **NotAllowed**
    * **NotFound**
    * **PaymentRestriction**
    * **Refusal**
    * **UnavailableDevice**
    * **UnavailableService**
    * **InvalidCard**
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


ErrorConditionOrStr: TypeAlias = Annotated[ErrorCondition | str, open_enum_validator(ErrorCondition)]
