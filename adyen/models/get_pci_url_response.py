from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class GetPciUrlResponse(SdkBaseModel):
    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Information about any invalid fields."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    redirect_url: Optional[str] = Field(default=UNSET, alias="redirectUrl")
    """The URL to the PCI compliance questionnaire where you should redirect your account holder. This URL must be used
    within 30 seconds and can only be used once."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetPciUrlResponseDict(TypedDict):
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    redirect_url: NotRequired[str]
    result_code: NotRequired[str]
