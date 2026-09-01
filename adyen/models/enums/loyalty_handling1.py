from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyHandling1(str, Enum):
    """Type of Loyalty processing requested by the Sale System. Possible values:
    * **Allowed**
    * **Forbidden**
    * **Processed**
    * **Proposed**
    * **Required**"""

    FORBIDDEN = "Forbidden"
    PROCESSED = "Processed"
    ALLOWED = "Allowed"
    PROPOSED = "Proposed"
    REQUIRED = "Required"

    __str__ = str.__str__


LoyaltyHandling1OrStr: TypeAlias = Annotated[LoyaltyHandling1 | str, open_enum_validator(LoyaltyHandling1)]
