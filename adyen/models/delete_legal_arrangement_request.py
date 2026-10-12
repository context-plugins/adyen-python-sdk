from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .legal_arrangement_request import LegalArrangementRequest, LegalArrangementRequestDict


class DeleteLegalArrangementRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder."""

    legal_arrangements: list[LegalArrangementRequest] = Field(alias="legalArrangements")
    """List of legal arrangements."""


class DeleteLegalArrangementRequestDict(TypedDict):
    account_holder_code: str
    legal_arrangements: list[LegalArrangementRequestDict]
