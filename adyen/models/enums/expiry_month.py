from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExpiryMonth(str, Enum):
    """Expiry month for the test card range.

    Allowed values:
    * JANUARY
    * FEBRUARY
    * MARCH
    * APRIL
    * MAY
    * JUNE
    * JULY
    * AUGUST
    * SEPTEMBER
    * OCTOBER
    * NOVEMBER
    * DECEMBER"""

    APRIL = "APRIL"
    AUGUST = "AUGUST"
    DECEMBER = "DECEMBER"
    FEBRUARY = "FEBRUARY"
    JANUARY = "JANUARY"
    JULY = "JULY"
    JUNE = "JUNE"
    MARCH = "MARCH"
    MAY = "MAY"
    NOVEMBER = "NOVEMBER"
    OCTOBER = "OCTOBER"
    SEPTEMBER = "SEPTEMBER"

    __str__ = str.__str__


ExpiryMonthOrStr: TypeAlias = Annotated[ExpiryMonth | str, open_enum_validator(ExpiryMonth)]
