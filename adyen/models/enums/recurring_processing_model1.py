from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecurringProcessingModel1(str, Enum):
    """Defines a recurring payment type. Required when creating a token to store payment details. Allowed values:
    * ``Subscription`` – A transaction for a fixed or variable amount, which follows a fixed schedule.
    * ``CardOnFile`` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel
        journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also
        considered a card-on-file transaction.
    * ``UnscheduledCardOnFile`` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a
        non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance
        drops below a certain amount."""

    CARD_ON_FILE = "CardOnFile"
    SUBSCRIPTION = "Subscription"
    UNSCHEDULED_CARD_ON_FILE = "UnscheduledCardOnFile"

    __str__ = str.__str__


RecurringProcessingModel1OrStr: TypeAlias = Annotated[
    RecurringProcessingModel1 | str, open_enum_validator(RecurringProcessingModel1)
]
