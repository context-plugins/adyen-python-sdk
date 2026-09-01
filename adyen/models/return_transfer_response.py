from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status62 import Status62OrStr


class ReturnTransferResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the return."""

    reference: Optional[str] = UNSET
    """Your internal reference for the return."""

    status: Optional[Status62OrStr] = UNSET
    """The resulting status of the return.

    Possible values: **Authorised**, **Declined**."""

    transfer_id: Optional[str] = Field(default=UNSET, alias="transferId")
    """The unique identifier of the original transfer."""


class ReturnTransferResponseDict(TypedDict):
    id: NotRequired[str]
    reference: NotRequired[str]
    status: NotRequired[Status62OrStr]
    transfer_id: NotRequired[str]
