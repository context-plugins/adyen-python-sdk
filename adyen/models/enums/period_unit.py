from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeriodUnit(str, Enum):
    """Type of instalment transaction. Possible values:
    * **Daily**
    * **Weekly**
    * **Monthly**
    * **Annual**"""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    ANNUAL = "Annual"

    __str__ = str.__str__


PeriodUnitOrStr: TypeAlias = Annotated[PeriodUnit | str, open_enum_validator(PeriodUnit)]
