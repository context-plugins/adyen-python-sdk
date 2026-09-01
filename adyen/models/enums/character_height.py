from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterHeight(str, Enum):
    """Possible values:
    * **SingleHeight**
    * **DoubleHeight**
    * **HalfHeight**"""

    SINGLE_HEIGHT = "SingleHeight"
    DOUBLE_HEIGHT = "DoubleHeight"
    HALF_HEIGHT = "HalfHeight"

    __str__ = str.__str__


CharacterHeightOrStr: TypeAlias = Annotated[CharacterHeight | str, open_enum_validator(CharacterHeight)]
