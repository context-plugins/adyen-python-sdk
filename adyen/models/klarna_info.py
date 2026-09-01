from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.region import RegionOrStr


class KlarnaInfo(SdkBaseModel):
    auto_capture: Optional[bool] = Field(default=UNSET, alias="autoCapture")
    """Indicates the status of `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__.
    Default value: **false**."""

    dispute_email: str = Field(alias="disputeEmail")
    """The email address for disputes."""

    region: RegionOrStr
    """The region of operation. For example, **NA**, **EU**, **CH**, **AU**."""

    support_email: str = Field(alias="supportEmail")
    """The email address of merchant support."""


class KlarnaInfoDict(TypedDict):
    auto_capture: NotRequired[bool]
    dispute_email: str
    region: RegionOrStr
    support_email: str
