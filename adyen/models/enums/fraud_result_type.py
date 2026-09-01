from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FraudResultType(str, Enum):
    """The fraud result properties of the payment. Possible values:
    * AMBER
    * GREEN
    * RED"""

    AMBER = "AMBER"
    GREEN = "GREEN"
    RED = "RED"

    __str__ = str.__str__


FraudResultTypeOrStr: TypeAlias = Annotated[FraudResultType | str, open_enum_validator(FraudResultType)]
