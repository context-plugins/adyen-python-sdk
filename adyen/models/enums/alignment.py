from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Alignment(str, Enum):
    """Possible values:
    * **Left**
    * **Right**
    * **Centred**
    * **Justified**"""

    LEFT = "Left"
    RIGHT = "Right"
    CENTRED = "Centred"
    JUSTIFIED = "Justified"

    __str__ = str.__str__


AlignmentOrStr: TypeAlias = Annotated[Alignment | str, open_enum_validator(Alignment)]
