from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type510 import Type510OrStr


class AdditionalBankIdentification1(SdkBaseModel):
    """Additional identification codes of the bank. Some banks may require these identifiers for cross-border
    transfers."""

    code: Optional[str] = UNSET
    """The value of the additional bank identification."""

    type_: Optional[Type510OrStr] = Field(default=UNSET, alias="type")
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


class AdditionalBankIdentification1Dict(TypedDict):
    code: NotRequired[str]
    type_: NotRequired[Type510OrStr]
