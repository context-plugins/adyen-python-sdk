from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .personal_document_data import PersonalDocumentData, PersonalDocumentDataDict


class ViasPersonalData1(SdkBaseModel):
    """Contains information about the person."""

    date_of_birth: Optional[str] = Field(default=UNSET, alias="dateOfBirth")
    """The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**."""

    document_data: Optional[list[PersonalDocumentData]] = Field(default=UNSET, alias="documentData")
    """Array that contains information about the person's identification document. You can submit only one entry per
    document type."""

    nationality: Optional[str] = UNSET
    """The nationality of the person represented by a two-character country code, in `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **NL**."""


class ViasPersonalData1Dict(TypedDict):
    date_of_birth: NotRequired[str]
    document_data: NotRequired[list[PersonalDocumentData | PersonalDocumentDataDict]]
    nationality: NotRequired[str]
