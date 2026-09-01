from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type113(str, Enum):
    """The type of transfer.

    Possible values:

     - **bankTransfer**: for push transfers to a transfer instrument or a bank account. The ``category`` must be
            **bank**.
    - **internalTransfer**: for push transfers between balance accounts. The ``category`` must be **internal**.
    - **internalDirectDebit**: for pull transfers (direct debits) between balance accounts. The ``category`` must be
        **internal**."""

    BANK_TRANSFER = "bankTransfer"
    INTERNAL_TRANSFER = "internalTransfer"
    INTERNAL_DIRECT_DEBIT = "internalDirectDebit"

    __str__ = str.__str__


Type113OrStr: TypeAlias = Annotated[Type113 | str, open_enum_validator(Type113)]
