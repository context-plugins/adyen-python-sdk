from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status3(str, Enum):
    """Status of the payment link. Possible values:
    * **active**: The link can be used to make payments.
    * **expired**: The expiry date for the payment link has passed. Shoppers can no longer use the link to make
        payments.
    * **completed**: The shopper completed the payment.
    * **paymentPending**: The shopper is in the process of making the payment. Applies to payment methods with an
        asynchronous flow."""

    ACTIVE = "active"
    COMPLETED = "completed"
    EXPIRED = "expired"
    PAID = "paid"
    PAYMENT_PENDING = "paymentPending"

    __str__ = str.__str__


Status3OrStr: TypeAlias = Annotated[Status3 | str, open_enum_validator(Status3)]
