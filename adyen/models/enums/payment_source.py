from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentSource(str, Enum):
    REDIRECT = "redirect"
    QR = "qr"
    PUSH_NOTIFICATION = "pushNotification"

    __str__ = str.__str__


PaymentSourceOrStr: TypeAlias = Annotated[PaymentSource | str, open_enum_validator(PaymentSource)]
