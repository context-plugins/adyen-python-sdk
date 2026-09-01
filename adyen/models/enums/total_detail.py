from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TotalDetail(str, Enum):
    POIID = "POIID"
    SALE_ID = "SaleID"
    OPERATOR_ID = "OperatorID"
    SHIFT_NUMBER = "ShiftNumber"
    TOTALS_GROUP_ID = "TotalsGroupID"

    __str__ = str.__str__


TotalDetailOrStr: TypeAlias = Annotated[TotalDetail | str, open_enum_validator(TotalDetail)]
