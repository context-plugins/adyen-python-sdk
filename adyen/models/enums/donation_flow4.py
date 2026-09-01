from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationFlow4(str, Enum):
    """The interaction flow for in-person donations: complete payment for the purchase and the donation in one go, or
    separately."""

    ONE_STEP = "oneStep"
    TWO_STEP = "twoStep"

    __str__ = str.__str__


DonationFlow4OrStr: TypeAlias = Annotated[DonationFlow4 | str, open_enum_validator(DonationFlow4)]
