from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Alignment1(str, Enum):
    """Alignment of the text string on the display line or print line. Absence of this data element means the characters
    have normal alignment. Possible values:
    * **Centred**
    * **Justified**
    * **Left**
    * **Right**"""

    LEFT = "Left"
    RIGHT = "Right"
    CENTRED = "Centred"
    JUSTIFIED = "Justified"

    __str__ = str.__str__


Alignment1OrStr: TypeAlias = Annotated[Alignment1 | str, open_enum_validator(Alignment1)]
