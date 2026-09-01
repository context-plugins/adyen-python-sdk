from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecurringProcessingModel7(str, Enum):
    """The processing model used for the recurring transaction."""

    CARD_ON_FILE = "CardOnFile"
    SUBSCRIPTION = "Subscription"
    UNSCHEDULED_CARD_ON_FILE = "UnscheduledCardOnFile"

    __str__ = str.__str__


RecurringProcessingModel7OrStr: TypeAlias = Annotated[
    RecurringProcessingModel7 | str, open_enum_validator(RecurringProcessingModel7)
]
