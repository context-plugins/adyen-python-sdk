from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Subtype(str, Enum):
    """The type of flow to initiate."""

    EXPRESS = "express"
    REDIRECT = "redirect"
    SDK = "sdk"

    __str__ = str.__str__


SubtypeOrStr: TypeAlias = Annotated[Subtype | str, open_enum_validator(Subtype)]
