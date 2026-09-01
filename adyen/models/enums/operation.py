from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Operation(str, Enum):
    """The type of string matching operation. Possible values: **startsWith**, **endsWith**, **isEqualTo**,
    **contains**,"""

    CONTAINS = "contains"
    ENDS_WITH = "endsWith"
    IS_EQUAL_TO = "isEqualTo"
    STARTS_WITH = "startsWith"

    __str__ = str.__str__


OperationOrStr: TypeAlias = Annotated[Operation | str, open_enum_validator(Operation)]
