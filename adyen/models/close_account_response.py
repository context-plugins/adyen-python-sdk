from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status22 import Status22OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class CloseAccountResponse(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The account code of the account that is closed."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""

    status: Optional[Status22OrStr] = UNSET
    """The new status of the account. >Permitted values: ``Active``, ``Inactive``, ``Suspended``, ``Closed``."""


class CloseAccountResponseDict(TypedDict):
    account_code: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    status: NotRequired[Status22OrStr]
