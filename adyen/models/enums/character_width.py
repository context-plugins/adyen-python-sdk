from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterWidth(str, Enum):
    """Possible values:
    * **SingleWidth**
    * **DoubleWidth**"""

    SINGLE_WIDTH = "SingleWidth"
    DOUBLE_WIDTH = "DoubleWidth"

    __str__ = str.__str__


CharacterWidthOrStr: TypeAlias = Annotated[CharacterWidth | str, open_enum_validator(CharacterWidth)]
