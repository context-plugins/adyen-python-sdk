from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Event(str, Enum):
    """The event. >Permitted values: ``InactivateAccount``, ``RefundNotPaidOutTransfers``. For more information, refer
    to `Verification checks <https://docs.adyen.com/classic-platforms/verification-process>`__."""

    INACTIVATE_ACCOUNT = "InactivateAccount"
    REFUND_NOT_PAID_OUT_TRANSFERS = "RefundNotPaidOutTransfers"

    __str__ = str.__str__


EventOrStr: TypeAlias = Annotated[Event | str, open_enum_validator(Event)]
