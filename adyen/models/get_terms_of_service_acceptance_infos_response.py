from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terms_of_service_acceptance_info import TermsOfServiceAcceptanceInfo, TermsOfServiceAcceptanceInfoDict


class GetTermsOfServiceAcceptanceInfosResponse(SdkBaseModel):
    data: Optional[list[TermsOfServiceAcceptanceInfo]] = UNSET
    """The Terms of Service acceptance information."""


class GetTermsOfServiceAcceptanceInfosResponseDict(TypedDict):
    data: NotRequired[list[TermsOfServiceAcceptanceInfo | TermsOfServiceAcceptanceInfoDict]]
