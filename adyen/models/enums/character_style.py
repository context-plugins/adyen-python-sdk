from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterStyle(str, Enum):
    """Possible values:
    * **Normal**
    * **Bold**
    * **Italic**
    * **Underline**"""

    NORMAL = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    UNDERLINE = "Underline"

    __str__ = str.__str__


CharacterStyleOrStr: TypeAlias = Annotated[CharacterStyle | str, open_enum_validator(CharacterStyle)]
