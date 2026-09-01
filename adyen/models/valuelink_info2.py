from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pin_support import PinSupportOrStr


class ValuelinkInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **valuelink**."""

    authorisation_mid: str = Field(alias="authorisationMid")
    """Authorisation Mid"""

    pin_support: PinSupportOrStr = Field(alias="pinSupport")
    """PIN Support. For ecommerce, PIN is required."""

    submitter_id: Optional[str] = Field(default=UNSET, alias="submitterId")
    """Submitter ID"""

    terminal_id: Optional[str] = Field(default=UNSET, alias="terminalId")
    """Terminal ID"""


class ValuelinkInfo2Dict(TypedDict):
    authorisation_mid: str
    pin_support: PinSupportOrStr
    submitter_id: NotRequired[str]
    terminal_id: NotRequired[str]
