from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.terms_of_service_type import TermsOfServiceTypeOrStr


class CalculateTermsOfServiceStatusResponse(SdkBaseModel):
    terms_of_service_types: Optional[list[TermsOfServiceTypeOrStr]] = Field(default=UNSET, alias="termsOfServiceTypes")
    """The type of Terms of Service that the legal entity needs to accept. If empty, no Terms of Service needs to be
    accepted."""


class CalculateTermsOfServiceStatusResponseDict(TypedDict):
    terms_of_service_types: NotRequired[list[TermsOfServiceTypeOrStr]]
