from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value5(str, Enum):
    BALANCE_ACCOUNT = "balanceAccount"
    BUSINESS_ACCOUNT = "businessAccount"

    __str__ = str.__str__


Value5OrStr: TypeAlias = Annotated[Value5 | str, open_enum_validator(Value5)]
