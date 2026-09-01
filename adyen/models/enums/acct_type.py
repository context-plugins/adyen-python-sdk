from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AcctType(str, Enum):
    """Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed
    values:
    * **01** — Not applicable
    * **02** — Credit
    * **03** — Debit"""

    _01 = "01"
    _02 = "02"
    _03 = "03"

    __str__ = str.__str__


AcctTypeOrStr: TypeAlias = Annotated[AcctType | str, open_enum_validator(AcctType)]
