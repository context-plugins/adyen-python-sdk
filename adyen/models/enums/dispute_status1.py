from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisputeStatus1(str, Enum):
    """The current status of the dispute.

    When you create a dispute, you can only set the ``status`` to **draft**. When you update a dispute, you can set the
    ``status`` to **submitted** or **closed**.

    Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**."""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    CHARGEBACK = "chargeback"
    SECOND_PRESENTMENT = "secondPresentment"
    WON = "won"
    CLOSED = "closed"

    __str__ = str.__str__


DisputeStatus1OrStr: TypeAlias = Annotated[DisputeStatus1 | str, open_enum_validator(DisputeStatus1)]
