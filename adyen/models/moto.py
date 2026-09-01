from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Moto(SdkBaseModel):
    enable_moto: Optional[bool] = Field(default=UNSET, alias="enableMoto")
    """Enable MOTO transactions."""

    max_amount: Optional[int] = Field(default=UNSET, alias="maxAmount")
    """The maximum amount for MOTO transactions. You need to set the currency for this amount using the
    https://docs.adyen.com/api-explorer/Management/1/patch/companies/(companyId/terminalSettings#request-standalone-currencyCode)
    parameter. Do not enable standalone, unless you are using a standalone solution."""


class MotoDict(TypedDict):
    enable_moto: NotRequired[bool]
    max_amount: NotRequired[int]
