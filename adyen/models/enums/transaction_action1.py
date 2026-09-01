from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionAction1(str, Enum):
    """Action to realise on a transaction. In an ``EnableService`` request message:
      - Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.
      - Aborts a swipe-ahead transaction or started by a ``CardAcquisition``, and not followed by a service request from
            the Sale System to complete the transaction.
    Possible values:
    * **AbortTransaction**
    * **StartTransaction**"""

    START_TRANSACTION = "StartTransaction"
    ABORT_TRANSACTION = "AbortTransaction"

    __str__ = str.__str__


TransactionAction1OrStr: TypeAlias = Annotated[TransactionAction1 | str, open_enum_validator(TransactionAction1)]
