from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyHandling2(str, Enum):
    """Type of Loyalty processing requested by the Sale System. An way to specify what the POI has to handle concerning
    the loyalty. Possible values:
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


LoyaltyHandling2OrStr: TypeAlias = Annotated[LoyaltyHandling2 | str, open_enum_validator(LoyaltyHandling2)]
