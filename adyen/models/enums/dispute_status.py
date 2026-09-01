from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisputeStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    CHARGEBACK = "chargeback"
    SECOND_PRESENTMENT = "secondPresentment"
    WON = "won"
    CLOSED = "closed"

    __str__ = str.__str__


DisputeStatusOrStr: TypeAlias = Annotated[DisputeStatus | str, open_enum_validator(DisputeStatus)]
