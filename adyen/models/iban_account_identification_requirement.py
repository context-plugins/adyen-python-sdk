from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IbanAccountIdentificationRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies the allowed prefixes for the international bank account number as defined in the ISO-13616 standard."""

    iban_prefixes: Optional[list[str]] = Field(default=UNSET, alias="ibanPrefixes")
    """Contains the list of allowed prefixes for international bank accounts. For example: NL, US, UK."""

    type_: Literal["ibanAccountIdentificationRequirement"] = Field(
        default="ibanAccountIdentificationRequirement", alias="type"
    )
    """**ibanAccountIdentificationRequirement**"""


class IbanAccountIdentificationRequirementDict(TypedDict):
    description: NotRequired[str]
    iban_prefixes: NotRequired[list[str]]
    type_: NotRequired[Literal["ibanAccountIdentificationRequirement"]]
