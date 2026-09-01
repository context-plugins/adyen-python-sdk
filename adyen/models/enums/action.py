from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Action(str, Enum):
    """Direction on how to handle any payouts that have already been scheduled.

    Possible values:
    * ``CLOSE``: close the existing batch of payouts.
    * ``UPDATE``: reschedule the existing batch to the new schedule.
    * ``NOTHING`` (**default**): allow the payout to proceed."""

    CLOSE = "CLOSE"
    NOTHING = "NOTHING"
    UPDATE = "UPDATE"

    __str__ = str.__str__


ActionOrStr: TypeAlias = Annotated[Action | str, open_enum_validator(Action)]
