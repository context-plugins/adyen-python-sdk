from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutSpeed4(str, Enum):
    """Speed at which payouts for this account are processed.

    Possible values: ``STANDARD``, ``SAME_DAY``."""

    INSTANT = "INSTANT"
    SAME_DAY = "SAME_DAY"
    STANDARD = "STANDARD"

    __str__ = str.__str__


PayoutSpeed4OrStr: TypeAlias = Annotated[PayoutSpeed4 | str, open_enum_validator(PayoutSpeed4)]
