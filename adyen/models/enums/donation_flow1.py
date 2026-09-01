from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationFlow1(str, Enum):
    """The interaction flow for in-person donations. Possible values:

    - **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the
        donation.

    - **twoStep**: The shopper presents their payment method twice: after the payment and after the donation."""

    ONE_STEP = "oneStep"
    TWO_STEP = "twoStep"

    __str__ = str.__str__


DonationFlow1OrStr: TypeAlias = Annotated[DonationFlow1 | str, open_enum_validator(DonationFlow1)]
