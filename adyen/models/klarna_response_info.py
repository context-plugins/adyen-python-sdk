from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.region1 import Region1OrStr


class KlarnaResponseInfo(SdkBaseModel):
    auto_capture: Optional[bool] = Field(default=UNSET, alias="autoCapture")
    """Indicates the status of `Automatic capture
    <https://docs.adyen.com/online-payments/capture#automatic-capture>`__."""

    dispute_email: Optional[str] = Field(default=UNSET, alias="disputeEmail")
    """The email address for disputes."""

    region: Optional[Region1OrStr] = UNSET
    """The region of operation."""

    support_email: Optional[str] = Field(default=UNSET, alias="supportEmail")
    """The email address of merchant support."""


class KlarnaResponseInfoDict(TypedDict):
    auto_capture: NotRequired[bool]
    dispute_email: NotRequired[str]
    region: NotRequired[Region1OrStr]
    support_email: NotRequired[str]
