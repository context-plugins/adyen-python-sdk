from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddrMatch(str, Enum):
    """Indicates whether the cardholder shipping address and cardholder billing address are the same. Allowed values:
    * **Y** — Shipping address matches billing address.
    * **N** — Shipping address does not match billing address."""

    Y = "Y"
    N = "N"

    __str__ = str.__str__


AddrMatchOrStr: TypeAlias = Annotated[AddrMatch | str, open_enum_validator(AddrMatch)]
