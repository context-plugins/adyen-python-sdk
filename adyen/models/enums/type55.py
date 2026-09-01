from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type55(str, Enum):
    """**visacheckout**"""

    VISACHECKOUT = "visacheckout"

    __str__ = str.__str__


Type55OrStr: TypeAlias = Annotated[Type55 | str, open_enum_validator(Type55)]
