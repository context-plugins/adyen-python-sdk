from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountStateType(str, Enum):
    """The state required for the account holder.
    > Permitted values: ``Processing``, ``Payout``."""

    LIMITED_PAYOUT = "LimitedPayout"
    LIMITED_PROCESSING = "LimitedProcessing"
    LIMITLESS_PAYOUT = "LimitlessPayout"
    LIMITLESS_PROCESSING = "LimitlessProcessing"
    PAYOUT = "Payout"
    PROCESSING = "Processing"

    __str__ = str.__str__


AccountStateTypeOrStr: TypeAlias = Annotated[AccountStateType | str, open_enum_validator(AccountStateType)]
