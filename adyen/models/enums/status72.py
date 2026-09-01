from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status72(str, Enum):
    """The status of the transaction.

     Possible values:

    * **pending**: The transaction is still pending.

    * **booked**: The transaction has been booked to the balance account."""

    BOOKED = "booked"
    PENDING = "pending"

    __str__ = str.__str__


Status72OrStr: TypeAlias = Annotated[Status72 | str, open_enum_validator(Status72)]
