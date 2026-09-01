from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type512(str, Enum):
    """The type of error.

    Possible values:
    * **invalidInput**
    * **dataMissing**
    * **pendingStatus**
    * **rejected**
    * **dataReview**"""

    DATA_MISSING = "dataMissing"
    DATA_REVIEW = "dataReview"
    INVALID_INPUT = "invalidInput"
    PENDING_STATUS = "pendingStatus"
    REJECTED = "rejected"

    __str__ = str.__str__


Type512OrStr: TypeAlias = Annotated[Type512 | str, open_enum_validator(Type512)]
