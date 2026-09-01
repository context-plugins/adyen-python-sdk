from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type46(str, Enum):
    """The payment method type."""

    PSE_PAYULATAM = "pse_payulatam"

    __str__ = str.__str__


Type46OrStr: TypeAlias = Annotated[Type46 | str, open_enum_validator(Type46)]
