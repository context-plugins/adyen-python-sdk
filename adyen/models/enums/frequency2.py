from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Frequency2(str, Enum):
    """The frequency at which the shopper will be charged."""

    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    HALF_YEARLY = "half-yearly"
    YEARLY = "yearly"

    __str__ = str.__str__


Frequency2OrStr: TypeAlias = Annotated[Frequency2 | str, open_enum_validator(Frequency2)]
