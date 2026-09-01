from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WeChatPayPosInfo(SdkBaseModel):
    contact_person_name: str = Field(alias="contactPersonName")
    """The name of the contact person from merchant support."""

    email: str
    """The email address of merchant support."""


class WeChatPayPosInfoDict(TypedDict):
    contact_person_name: str
    email: str
