from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type511(str, Enum):
    """**issuedCard**"""

    ISSUED_CARD = "issuedCard"

    __str__ = str.__str__


Type511OrStr: TypeAlias = Annotated[Type511 | str, open_enum_validator(Type511)]
