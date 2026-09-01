from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type58(str, Enum):
    """**zip**"""

    ZIP = "zip"
    ZIP_POS = "zip_pos"

    __str__ = str.__str__


Type58OrStr: TypeAlias = Annotated[Type58 | str, open_enum_validator(Type58)]
