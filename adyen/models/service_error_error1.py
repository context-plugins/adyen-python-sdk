from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceErrorError1(SdkBaseModel):
    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """The error code mapped to the error message."""

    error_type: Optional[str] = Field(default=UNSET, alias="errorType")
    """The category of the error."""

    message: Optional[str] = UNSET
    """A short explanation of the issue."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The PSP reference of the payment."""

    status: Optional[int] = UNSET
    """The HTTP response status."""


class ServiceErrorError1Dict(TypedDict):
    error_code: NotRequired[str]
    error_type: NotRequired[str]
    message: NotRequired[str]
    psp_reference: NotRequired[str]
    status: NotRequired[int]
