from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterWidth1(str, Enum):
    """Character width of the text string to display or print. Absence of this data element means the characters have
    normal width. Possible values:
    * **DoubleWidth**
    * **SingleWidth**"""

    SINGLE_WIDTH = "SingleWidth"
    DOUBLE_WIDTH = "DoubleWidth"

    __str__ = str.__str__


CharacterWidth1OrStr: TypeAlias = Annotated[CharacterWidth1 | str, open_enum_validator(CharacterWidth1)]
