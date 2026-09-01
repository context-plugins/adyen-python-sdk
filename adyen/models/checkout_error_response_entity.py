from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutErrorResponseEntity(SdkBaseModel):
    error_code: str = Field(alias="errorCode")
    error_type: str = Field(alias="errorType")
    message: str
    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    status: Optional[int] = UNSET


class CheckoutErrorResponseEntityDict(TypedDict):
    error_code: str
    error_type: str
    message: str
    psp_reference: NotRequired[str]
    status: NotRequired[int]
