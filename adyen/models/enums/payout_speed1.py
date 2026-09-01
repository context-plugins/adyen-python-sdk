from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutSpeed1(str, Enum):
    """Speed at which payouts for this account are processed.

    Possible values: ``STANDARD`` (default), ``SAME_DAY``."""

    INSTANT = "INSTANT"
    SAME_DAY = "SAME_DAY"
    STANDARD = "STANDARD"

    __str__ = str.__str__


PayoutSpeed1OrStr: TypeAlias = Annotated[PayoutSpeed1 | str, open_enum_validator(PayoutSpeed1)]
