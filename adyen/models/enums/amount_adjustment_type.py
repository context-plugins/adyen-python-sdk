from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AmountAdjustmentType(str, Enum):
    """The type of markup that is applied to an authorised payment.

    Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**."""

    ATM_MARKUP = "atmMarkup"
    AUTH_HOLD_RESERVE = "authHoldReserve"
    EXCHANGE = "exchange"
    FOREX_MARKUP = "forexMarkup"

    __str__ = str.__str__


AmountAdjustmentTypeOrStr: TypeAlias = Annotated[AmountAdjustmentType | str, open_enum_validator(AmountAdjustmentType)]
