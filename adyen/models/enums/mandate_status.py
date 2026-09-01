from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MandateStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CANCELLED = "cancelled"

    __str__ = str.__str__


MandateStatusOrStr: TypeAlias = Annotated[MandateStatus | str, open_enum_validator(MandateStatus)]
