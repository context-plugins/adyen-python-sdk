from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Company1(SdkBaseModel):
    """Information regarding the company."""

    homepage: Optional[str] = UNSET
    """The company website's home page."""

    name: Optional[str] = UNSET
    """The company name."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """Registration number of the company."""

    registry_location: Optional[str] = Field(default=UNSET, alias="registryLocation")
    """Registry location of the company."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """Tax ID of the company."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The company type."""


class Company1Dict(TypedDict):
    homepage: NotRequired[str]
    name: NotRequired[str]
    registration_number: NotRequired[str]
    registry_location: NotRequired[str]
    tax_id: NotRequired[str]
    type_: NotRequired[str]
