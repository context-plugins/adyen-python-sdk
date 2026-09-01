from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceError(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some data fields are included only if you select them first.
    Go to **Customer Area** > **Developers** > **Additional data**."""

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


class ServiceErrorDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    error_code: NotRequired[str]
    error_type: NotRequired[str]
    message: NotRequired[str]
    psp_reference: NotRequired[str]
    status: NotRequired[int]
