from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransType(str, Enum):
    """Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values:
    * **01** — Goods/Service Purchase
    * **03** — Check Acceptance
    * **10** — Account Funding
    * **11** — Quasi-Cash Transaction
    * **28** — Prepaid Activation and Load"""

    _01 = "01"
    _03 = "03"
    _10 = "10"
    _11 = "11"
    _28 = "28"

    __str__ = str.__str__


TransTypeOrStr: TypeAlias = Annotated[TransType | str, open_enum_validator(TransType)]
