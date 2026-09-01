from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoreFiltrationMode(str, Enum):
    """Specifies how payment methods should be filtered based on the 'store' parameter:
      - 'exclusive': Only payment methods belonging to the specified 'store' are returned.
      - 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned."""

    EXCLUSIVE = "exclusive"
    INCLUSIVE = "inclusive"
    SKIP_FILTER = "skipFilter"

    __str__ = str.__str__


StoreFiltrationModeOrStr: TypeAlias = Annotated[StoreFiltrationMode | str, open_enum_validator(StoreFiltrationMode)]
