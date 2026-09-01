from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyHandling(str, Enum):
    """Possible values:
    * **Forbidden**
    * **Processed**
    * **Allowed**
    * **Proposed**
    * **Required**"""

    FORBIDDEN = "Forbidden"
    PROCESSED = "Processed"
    ALLOWED = "Allowed"
    PROPOSED = "Proposed"
    REQUIRED = "Required"

    __str__ = str.__str__


LoyaltyHandlingOrStr: TypeAlias = Annotated[LoyaltyHandling | str, open_enum_validator(LoyaltyHandling)]
