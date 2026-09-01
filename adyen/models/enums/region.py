from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Region(str, Enum):
    """The region of operation. For example, **NA**, **EU**, **CH**, **AU**."""

    NA = "NA"
    EU = "EU"
    CH = "CH"
    AU = "AU"

    __str__ = str.__str__


RegionOrStr: TypeAlias = Annotated[Region | str, open_enum_validator(Region)]
