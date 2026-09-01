from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Summary(SdkBaseModel):
    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the legal entity."""

    tax_years: list[int] = Field(alias="taxYears")
    """The tax years for which the legal entity has a tax form."""


class SummaryDict(TypedDict):
    legal_entity_id: str
    tax_years: list[int]
