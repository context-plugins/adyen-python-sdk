from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MandateStatus2(str, Enum):
    """The status of the mandate.

    Possible values: **pending**, **approved**, **cancelled**."""

    PENDING = "pending"
    APPROVED = "approved"
    CANCELLED = "cancelled"

    __str__ = str.__str__


MandateStatus2OrStr: TypeAlias = Annotated[MandateStatus2 | str, open_enum_validator(MandateStatus2)]
