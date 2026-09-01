from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeriodUnit1(str, Enum):
    """Type of instalment transaction. Possible values:
    * **Annual**
    * **Daily**
    * **Monthly**
    * **Weekly**"""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    ANNUAL = "Annual"

    __str__ = str.__str__


PeriodUnit1OrStr: TypeAlias = Annotated[PeriodUnit1 | str, open_enum_validator(PeriodUnit1)]
