from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckTaxElectronicDeliveryConsentResponse(SdkBaseModel):
    us1099k: Optional[bool] = Field(default=UNSET, alias="US1099k")
    """Consent to electronically deliver tax form US1099-K."""


class CheckTaxElectronicDeliveryConsentResponseDict(TypedDict):
    us1099k: NotRequired[bool]
