from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ModifyRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular payout request."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    original_reference: str = Field(alias="originalReference")
    """The PSP reference received in the ``/submitThirdParty`` response."""


class ModifyRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    merchant_account: str
    original_reference: str
