from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RateType(str, Enum):
    """Indicates whether the rental rate is daily or weekly.
    * **additionalData key:** ``carRental.rateIndicator``"""

    DAILY = "daily"
    WEEKLY = "weekly"

    __str__ = str.__str__


RateTypeOrStr: TypeAlias = Annotated[RateType | str, open_enum_validator(RateType)]
