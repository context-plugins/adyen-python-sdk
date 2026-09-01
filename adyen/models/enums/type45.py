from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type45(str, Enum):
    """**paybybank_pix**"""

    PAYBYBANK_PIX = "paybybank_pix"

    __str__ = str.__str__


Type45OrStr: TypeAlias = Annotated[Type45 | str, open_enum_validator(Type45)]
