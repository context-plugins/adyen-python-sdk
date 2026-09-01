from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LegalArrangementRequest(SdkBaseModel):
    legal_arrangement_code: str = Field(alias="legalArrangementCode")
    """The code of the legal arrangement to be deleted. If you also send ``legalArrangementEntityCodes``, only the
    entities listed will be deleted."""

    legal_arrangement_entity_codes: Optional[list[str]] = Field(default=UNSET, alias="legalArrangementEntityCodes")
    """List of legal arrangement entities to be deleted."""


class LegalArrangementRequestDict(TypedDict):
    legal_arrangement_code: str
    legal_arrangement_entity_codes: NotRequired[list[str]]
