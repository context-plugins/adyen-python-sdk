from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisplayTextField2(str, Enum):
    """The text shown on the payment terminal, either the name or the cause of the nonprofit organization."""

    CAUSE_NAME = "causeName"
    NONPROFIT_NAME = "nonprofitName"

    __str__ = str.__str__


DisplayTextField2OrStr: TypeAlias = Annotated[DisplayTextField2 | str, open_enum_validator(DisplayTextField2)]
