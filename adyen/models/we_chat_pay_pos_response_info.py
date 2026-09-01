from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WeChatPayPosResponseInfo(SdkBaseModel):
    contact_person_name: Optional[str] = Field(default=UNSET, alias="contactPersonName")
    """The name of the contact person from merchant support."""

    email: Optional[str] = UNSET
    """The email address of merchant support."""


class WeChatPayPosResponseInfoDict(TypedDict):
    contact_person_name: NotRequired[str]
    email: NotRequired[str]
