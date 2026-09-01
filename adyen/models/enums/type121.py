from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type121(str, Enum):
    """The type of the cashout transfer.

    Possible values:
    - **cashoutRepayment**: Corresponds to the transfer created to deduct the cashout amount after settlement.
    - **cashoutFee**: Corresponds to the transfer created to debit the cashout fee form the user's balance account."""

    CASHOUT_REPAYMENT = "cashoutRepayment"
    CASHOUT_FEE = "cashoutFee"

    __str__ = str.__str__


Type121OrStr: TypeAlias = Annotated[Type121 | str, open_enum_validator(Type121)]
