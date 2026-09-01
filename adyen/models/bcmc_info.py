from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BcmcInfo(SdkBaseModel):
    enable_bcmc_mobile: Optional[bool] = Field(default=UNSET, alias="enableBcmcMobile")
    """Indicates if `Bancontact mobile <https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile>`__ is
    enabled."""


class BcmcInfoDict(TypedDict):
    enable_bcmc_mobile: NotRequired[bool]
