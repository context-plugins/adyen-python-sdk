from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentSource2(str, Enum):
    """The source used to obtain the payload. Possible values: ``qr``, ``redirect``, and ``pushNotification``."""

    REDIRECT = "redirect"
    QR = "qr"
    PUSH_NOTIFICATION = "pushNotification"

    __str__ = str.__str__


PaymentSource2OrStr: TypeAlias = Annotated[PaymentSource2 | str, open_enum_validator(PaymentSource2)]
