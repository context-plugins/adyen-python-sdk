from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationFlow(str, Enum):
    ONE_STEP = "oneStep"
    TWO_STEP = "twoStep"

    __str__ = str.__str__


DonationFlowOrStr: TypeAlias = Annotated[DonationFlow | str, open_enum_validator(DonationFlow)]
