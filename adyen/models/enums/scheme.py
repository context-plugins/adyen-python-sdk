from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Scheme(str, Enum):
    """The Secure Remote Commerce scheme."""

    MC = "mc"
    VISA = "visa"

    __str__ = str.__str__


SchemeOrStr: TypeAlias = Annotated[Scheme | str, open_enum_validator(Scheme)]
