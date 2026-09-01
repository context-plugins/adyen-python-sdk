from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.response import ResponseOrStr


class ModificationResult(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be returned in a particular modification response."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character string reference associated with the transaction/request. This value is globally unique;
    quote it when communicating with us about this request."""

    response: ResponseOrStr
    """Indicates if the modification request has been received for processing."""


class ModificationResultDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    psp_reference: str
    response: ResponseOrStr
