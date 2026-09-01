from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SuspiciousAccActivity(str, Enum):
    """Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the
    cardholder account. Allowed values:
    * **01** — No suspicious activity has been observed
    * **02** — Suspicious activity has been observed"""

    _01 = "01"
    _02 = "02"

    __str__ = str.__str__


SuspiciousAccActivityOrStr: TypeAlias = Annotated[
    SuspiciousAccActivity | str, open_enum_validator(SuspiciousAccActivity)
]
