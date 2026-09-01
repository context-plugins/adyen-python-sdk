from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RequestActivationResponse(SdkBaseModel):
    company_id: Optional[str] = Field(default=UNSET, alias="companyId")
    """The unique identifier of the company account."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant account you requested to activate."""


class RequestActivationResponseDict(TypedDict):
    company_id: NotRequired[str]
    merchant_id: NotRequired[str]
