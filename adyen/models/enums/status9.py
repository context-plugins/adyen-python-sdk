from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status9(str, Enum):
    """The status of the account holder.

    Possible values:

     * **active**: The account holder is active and allowed to use its capabilities. This is the initial status for
            account holders and balance accounts. You can change this status to **suspended** or **closed**.

     * **suspended**: The account holder is temporarily disabled and payouts are blocked. You can change this status to
            **active** or **closed**.

    * **closed**: The account holder and all of its capabilities are permanently disabled. This is a final status and
        cannot be changed."""

    ACTIVE = "active"
    CLOSED = "closed"
    SUSPENDED = "suspended"

    __str__ = str.__str__


Status9OrStr: TypeAlias = Annotated[Status9 | str, open_enum_validator(Status9)]
