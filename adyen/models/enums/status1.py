from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1(str, Enum):
    """The status of the donation transaction.

    Possible values:
    * **completed**
    * **pending**
    * **refused**"""

    COMPLETED = "completed"
    PENDING = "pending"
    REFUSED = "refused"

    __str__ = str.__str__


Status1OrStr: TypeAlias = Annotated[Status1 | str, open_enum_validator(Status1)]
