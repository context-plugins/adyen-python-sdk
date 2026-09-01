from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Behavior(str, Enum):
    """The method of handling the chargeback.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**.,
    Specifies how and from which balance account(s) to deduct the chargeback amount.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**.,
    Specifies how and from which balance account(s) to deduct the refund amount.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**"""

    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"
    DEDUCT_ACCORDING_TO_SPLIT_RATIO = "deductAccordingToSplitRatio"
    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"

    __str__ = str.__str__


BehaviorOrStr: TypeAlias = Annotated[Behavior | str, open_enum_validator(Behavior)]
