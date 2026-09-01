from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChAccPwChangeInd(str, Enum):
    """Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or
    account reset. Allowed values:
    * **01** — No change
    * **02** — Changed during this transaction
    * **03** — Less than 30 days
    * **04** — 30–60 days
    * **05** — More than 60 days"""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"

    __str__ = str.__str__


ChAccPwChangeIndOrStr: TypeAlias = Annotated[ChAccPwChangeInd | str, open_enum_validator(ChAccPwChangeInd)]
