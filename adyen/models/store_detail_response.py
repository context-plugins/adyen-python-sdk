from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoreDetailResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be returned in a particular response."""

    psp_reference: str = Field(alias="pspReference")
    """A new reference to uniquely identify this request."""

    recurring_detail_reference: str = Field(alias="recurringDetailReference")
    """The token which you can use later on for submitting the payout."""

    result_code: str = Field(alias="resultCode")
    """The result code of the transaction. ``Success`` indicates that the details were stored successfully."""


class StoreDetailResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    psp_reference: str
    recurring_detail_reference: str
    result_code: str
