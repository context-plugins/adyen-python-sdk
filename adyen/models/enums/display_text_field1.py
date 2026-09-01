from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisplayTextField1(str, Enum):
    """The text shown on the payment terminal, asking the shopper for a donation."""

    CAUSE_NAME = "causeName"
    NONPROFIT_NAME = "nonprofitName"

    __str__ = str.__str__


DisplayTextField1OrStr: TypeAlias = Annotated[DisplayTextField1 | str, open_enum_validator(DisplayTextField1)]
