from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Result3(str, Enum):
    """Possible values:
    * **Success**
    * **Failure**
    * **Partial**"""

    SUCCESS = "Success"
    FAILURE = "Failure"
    PARTIAL = "Partial"

    __str__ = str.__str__


Result3OrStr: TypeAlias = Annotated[Result3 | str, open_enum_validator(Result3)]
