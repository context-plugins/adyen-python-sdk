from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisplayTextField(str, Enum):
    CAUSE_NAME = "causeName"
    NONPROFIT_NAME = "nonprofitName"

    __str__ = str.__str__


DisplayTextFieldOrStr: TypeAlias = Annotated[DisplayTextField | str, open_enum_validator(DisplayTextField)]
