from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GlobalStatus1(str, Enum):
    """Global status of a POI Server or POI Terminal. Possible values:
    * **Busy**
    * **Maintenance**
    * **OK**
    * **Unreachable**"""

    OK = "OK"
    BUSY = "Busy"
    MAINTENANCE = "Maintenance"
    UNREACHABLE = "Unreachable"

    __str__ = str.__str__


GlobalStatus1OrStr: TypeAlias = Annotated[GlobalStatus1 | str, open_enum_validator(GlobalStatus1)]
