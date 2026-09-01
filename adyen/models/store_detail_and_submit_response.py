from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoreDetailAndSubmitResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be returned in a particular response."""

    psp_reference: str = Field(alias="pspReference")
    """A new reference to uniquely identify this request."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """In case of refusal, an informational message for the reason."""

    result_code: str = Field(alias="resultCode")
    """The response:

    * In case of success is payout-submit-received.
    * In case of an error, an informational message is returned."""


class StoreDetailAndSubmitResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    psp_reference: str
    refusal_reason: NotRequired[str]
    result_code: str
