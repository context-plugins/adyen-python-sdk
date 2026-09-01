from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DataOnly(str, Enum):
    """Required to trigger the `data-only flow <https://docs.adyen.com/online-payments/3d-secure/data-only/>`__. When
    set to **true**, forces the 3D Secure 2 data-only flow for all transactions where it is possible."""

    FALSE = "false"
    TRUE = "true"

    __str__ = str.__str__


DataOnlyOrStr: TypeAlias = Annotated[DataOnly | str, open_enum_validator(DataOnly)]
