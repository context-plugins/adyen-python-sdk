from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type212(str, Enum):
    """The type of error.



    Possible values:
    * **invalidInput**
    * **dataMissing**
    * **pendingStatus**
    * **dataReview**"""

    DATA_MISSING = "dataMissing"
    DATA_REVIEW = "dataReview"
    INVALID_INPUT = "invalidInput"
    PENDING_STATUS = "pendingStatus"

    __str__ = str.__str__


Type212OrStr: TypeAlias = Annotated[Type212 | str, open_enum_validator(Type212)]
