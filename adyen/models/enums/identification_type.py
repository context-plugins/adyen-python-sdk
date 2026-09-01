from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentificationType(str, Enum):
    """The type of the identification.

    Possible values: **iban**, **routingNumber**, **sortCode**, **bic**."""

    BIC = "bic"
    IBAN = "iban"
    ROUTING_NUMBER = "routingNumber"
    SORT_CODE = "sortCode"

    __str__ = str.__str__


IdentificationTypeOrStr: TypeAlias = Annotated[IdentificationType | str, open_enum_validator(IdentificationType)]
