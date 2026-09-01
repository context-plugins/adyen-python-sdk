from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GlobalStatus(str, Enum):
    """Possible values:
    * **OK**
    * **Busy**
    * **Maintenance**
    * **Unreachable**"""

    OK = "OK"
    BUSY = "Busy"
    MAINTENANCE = "Maintenance"
    UNREACHABLE = "Unreachable"

    __str__ = str.__str__


GlobalStatusOrStr: TypeAlias = Annotated[GlobalStatus | str, open_enum_validator(GlobalStatus)]
