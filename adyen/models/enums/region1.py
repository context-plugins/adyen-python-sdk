from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Region1(str, Enum):
    """The region of operation."""

    AU = "AU"
    CH = "CH"
    EU = "EU"
    NA = "NA"

    __str__ = str.__str__


Region1OrStr: TypeAlias = Annotated[Region1 | str, open_enum_validator(Region1)]
