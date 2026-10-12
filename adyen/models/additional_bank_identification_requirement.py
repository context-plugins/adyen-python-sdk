from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.additional_bank_identification_type import AdditionalBankIdentificationTypeOrStr


class AdditionalBankIdentificationRequirement(SdkBaseModel):
    additional_bank_identification_type: Optional[AdditionalBankIdentificationTypeOrStr] = Field(
        default=UNSET, alias="additionalBankIdentificationType"
    )
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

    description: Optional[str] = UNSET
    """The description of the additional bank identification requirement."""

    type_: Literal["additionalBankIdentificationRequirement"] = Field(
        default="additionalBankIdentificationRequirement", alias="type"
    )
    """**additionalBankIdentificationRequirement**"""


class AdditionalBankIdentificationRequirementDict(TypedDict):
    additional_bank_identification_type: NotRequired[AdditionalBankIdentificationTypeOrStr]
    description: NotRequired[str]
    type_: Literal["additionalBankIdentificationRequirement"]
