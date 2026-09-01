from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pin_support import PinSupportOrStr


class ValuelinkResponseInfo(SdkBaseModel):
    authorisation_mid: Optional[str] = Field(default=UNSET, alias="authorisationMid")
    """Authorisation Mid"""

    pin_support: Optional[PinSupportOrStr] = Field(default=UNSET, alias="pinSupport")
    """PIN Support. For ecommerce, PIN is required."""

    submitter_id: Optional[str] = Field(default=UNSET, alias="submitterId")
    """Submitter ID"""

    terminal_id: Optional[str] = Field(default=UNSET, alias="terminalId")
    """Terminal ID"""


class ValuelinkResponseInfoDict(TypedDict):
    authorisation_mid: NotRequired[str]
    pin_support: NotRequired[PinSupportOrStr]
    submitter_id: NotRequired[str]
    terminal_id: NotRequired[str]
