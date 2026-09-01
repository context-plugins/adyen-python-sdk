from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status24 import Status24OrStr


class Modification2(SdkBaseModel):
    """The payment modification. Only applicable for `returned internal transfers
    <https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks/#returned-internal-transfer>`__."""

    direction: Optional[str] = UNSET
    """The direction of the money movement."""

    id: Optional[str] = UNSET
    """Our reference for the modification."""

    reference: Optional[str] = UNSET
    """Your reference for the modification, used internally within your platform."""

    status: Optional[Status24OrStr] = UNSET
    """The status of the transfer event."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of transfer modification."""


class Modification2Dict(TypedDict):
    direction: NotRequired[str]
    id: NotRequired[str]
    reference: NotRequired[str]
    status: NotRequired[Status24OrStr]
    type_: NotRequired[str]
