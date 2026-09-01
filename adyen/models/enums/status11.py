from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status11(str, Enum):
    """The status of the store. Possible values are:

    - **active**. This value is assigned automatically when a store is created.
    - **inactive**. The terminals under the store are blocked from accepting new transactions, but capturing outstanding
        transactions is still possible.
    - **closed**. This status is irreversible. The terminals under the store are reassigned to the merchant
        inventory."""

    ACTIVE = "active"
    CLOSED = "closed"
    INACTIVE = "inactive"

    __str__ = str.__str__


Status11OrStr: TypeAlias = Annotated[Status11 | str, open_enum_validator(Status11)]
