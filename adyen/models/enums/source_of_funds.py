from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SourceOfFunds(str, Enum):
    """Indicates where the funds used for the transfer originated. Possible values are:
    - **DEBIT** for card-to-card transfers.
    - **DEPOSIT_ACCOUNT** for wallet-to-card transfers."""

    DEBIT = "DEBIT"
    DEPOSIT_ACCOUNT = "DEPOSIT_ACCOUNT"

    __str__ = str.__str__


SourceOfFundsOrStr: TypeAlias = Annotated[SourceOfFunds | str, open_enum_validator(SourceOfFunds)]
