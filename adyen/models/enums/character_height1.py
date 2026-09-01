from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterHeight1(str, Enum):
    """Character height of the text string to display or print. Absence of this data element means the characters have
    normal height. Possible values:
    * **DoubleHeight**
    * **HalfHeight**
    * **SingleHeight**"""

    SINGLE_HEIGHT = "SingleHeight"
    DOUBLE_HEIGHT = "DoubleHeight"
    HALF_HEIGHT = "HalfHeight"

    __str__ = str.__str__


CharacterHeight1OrStr: TypeAlias = Annotated[CharacterHeight1 | str, open_enum_validator(CharacterHeight1)]
