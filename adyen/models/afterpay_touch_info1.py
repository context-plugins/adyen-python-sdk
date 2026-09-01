from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AfterpayTouchInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **afterpaytouch**."""

    support_email: Optional[str] = Field(default=UNSET, alias="supportEmail")
    """Support Email"""

    support_url: str = Field(alias="supportUrl")
    """Support Url"""


class AfterpayTouchInfo1Dict(TypedDict):
    support_email: NotRequired[str]
    support_url: str
