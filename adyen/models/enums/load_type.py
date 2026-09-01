from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoadType(str, Enum):
    """The type of load you are trying to do, when absent we default to 'load'"""

    MERCHANDISE_RETURN = "merchandiseReturn"
    LOAD = "load"

    __str__ = str.__str__


LoadTypeOrStr: TypeAlias = Annotated[LoadType | str, open_enum_validator(LoadType)]
