from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TaxInformation(SdkBaseModel):
    country: Optional[str] = UNSET
    """The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code."""

    number: Optional[str] = UNSET
    """The tax ID number (TIN) of the organization or individual."""

    number_absent: Optional[bool] = Field(default=UNSET, alias="numberAbsent")
    """Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only
    applicable in Australia."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs:
    Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US."""


class TaxInformationDict(TypedDict):
    country: NotRequired[str]
    number: NotRequired[str]
    number_absent: NotRequired[bool]
    type_: NotRequired[str]
