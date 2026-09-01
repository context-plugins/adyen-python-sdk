from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IndustryUsage1(str, Enum):
    """The reason for the amount update. Possible values:
    * **delayedCharge**
    * **noShow**
    * **installment**"""

    DELAYED_CHARGE = "delayedCharge"
    INSTALLMENT = "installment"
    NO_SHOW = "noShow"

    __str__ = str.__str__


IndustryUsage1OrStr: TypeAlias = Annotated[IndustryUsage1 | str, open_enum_validator(IndustryUsage1)]
