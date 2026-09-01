from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutSpeed(str, Enum):
    """Speed with which payouts for this account are processed. Permitted values: ``STANDARD``, ``SAME_DAY``."""

    INSTANT = "INSTANT"
    SAME_DAY = "SAME_DAY"
    STANDARD = "STANDARD"

    __str__ = str.__str__


PayoutSpeedOrStr: TypeAlias = Annotated[PayoutSpeed | str, open_enum_validator(PayoutSpeed)]
