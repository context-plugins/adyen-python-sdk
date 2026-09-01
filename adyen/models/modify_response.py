from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ModifyResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be returned in a particular response."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character string reference associated with the transaction. This value is globally unique; quote it
    when communicating with us about this response."""

    response: str
    """The response:
    * In case of success, it is either ``payout-confirm-received`` or ``payout-decline-received``.
    * In case of an error, an informational message is returned."""


class ModifyResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    psp_reference: str
    response: str
