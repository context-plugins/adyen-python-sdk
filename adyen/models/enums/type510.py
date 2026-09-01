from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type510(str, Enum):
    """The type of additional bank identification, depending on the country.

    Possible values:

     * **auBsbCode**: The 6-digit `Australian Bank State Branch (BSB) code
            <https://en.wikipedia.org/wiki/Bank_state_branch>`__, without separators or spaces.
     * **caRoutingNumber**: The 9-digit `Canadian routing number
            <https://en.wikipedia.org/wiki/Routing_number_(Canada>`__), in EFT format, without separators or spaces.
     * **gbSortCode**: The 6-digit `UK sort code <https://en.wikipedia.org/wiki/Sort_code>`__, without separators or
            spaces
     * **usRoutingNumber**: The 9-digit `routing number <https://en.wikipedia.org/wiki/ABA_routing_transit_number>`__,
            without separators or spaces."""

    AU_BSB_CODE = "auBsbCode"
    CA_ROUTING_NUMBER = "caRoutingNumber"
    GB_SORT_CODE = "gbSortCode"
    US_ROUTING_NUMBER = "usRoutingNumber"

    __str__ = str.__str__


Type510OrStr: TypeAlias = Annotated[Type510 | str, open_enum_validator(Type510)]
