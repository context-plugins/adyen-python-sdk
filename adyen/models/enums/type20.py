from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type20(str, Enum):
    """**dbarai**"""

    DBARAI = "dbarai"

    __str__ = str.__str__


Type20OrStr: TypeAlias = Annotated[Type20 | str, open_enum_validator(Type20)]
