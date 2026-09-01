from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LimitStatus(str, Enum):
    """The status of the transfer limit. Possible values:
    * **active**: the limit is currently active.
    * **inactive**: the limit is currently inactive.
    * **pendingSCA**: the limit is pending until your user performs SCA.
    * **scheduled**: the limit is scheduled to become active at a future date."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING_SCA = "pendingSCA"
    SCHEDULED = "scheduled"

    __str__ = str.__str__


LimitStatusOrStr: TypeAlias = Annotated[LimitStatus | str, open_enum_validator(LimitStatus)]
