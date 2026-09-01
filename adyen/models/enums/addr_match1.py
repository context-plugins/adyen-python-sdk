from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddrMatch1(str, Enum):
    """Indicates whether the cardholder shipping Address and cardholder billing address are the same. Allowed values:
    * **Y** — Shipping Address matches Billing Address.
    * **N** — Shipping Address does not match Billing Address."""

    Y = "Y"
    N = "N"

    __str__ = str.__str__


AddrMatch1OrStr: TypeAlias = Annotated[AddrMatch1 | str, open_enum_validator(AddrMatch1)]
