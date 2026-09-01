from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Result11(str, Enum):
    """Result of the processing of the message. Possible values:
    * **Failure**
    * **Partial**
    * **Success**"""

    SUCCESS = "Success"
    FAILURE = "Failure"
    PARTIAL = "Partial"

    __str__ = str.__str__


Result11OrStr: TypeAlias = Annotated[Result11 | str, open_enum_validator(Result11)]
