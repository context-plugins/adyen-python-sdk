from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AfterpayTouchResponseInfo1(SdkBaseModel):
    """**afterpaytouch** details"""

    support_email: Optional[str] = Field(default=UNSET, alias="supportEmail")
    """Support Email"""

    support_url: Optional[str] = Field(default=UNSET, alias="supportUrl")
    """Support Url"""


class AfterpayTouchResponseInfo1Dict(TypedDict):
    support_email: NotRequired[str]
    support_url: NotRequired[str]
