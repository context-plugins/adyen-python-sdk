from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type82(str, Enum):
    """**sgLocal**"""

    SG_LOCAL = "sgLocal"

    __str__ = str.__str__


Type82OrStr: TypeAlias = Annotated[Type82 | str, open_enum_validator(Type82)]
