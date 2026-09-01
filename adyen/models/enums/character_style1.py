from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CharacterStyle1(str, Enum):
    """Typographic style of the sequence of characters to display or print. Absence of this data element means the
    characters have normal style. Possible values:
    * **Bold**
    * **Italic**
    * **Normal**
    * **Underline**"""

    NORMAL = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    UNDERLINE = "Underline"

    __str__ = str.__str__


CharacterStyle1OrStr: TypeAlias = Annotated[CharacterStyle1 | str, open_enum_validator(CharacterStyle1)]
