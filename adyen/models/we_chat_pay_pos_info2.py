from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WeChatPayPosInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **wechatpay_pos**."""

    contact_person_name: str = Field(alias="contactPersonName")
    """The name of the contact person from merchant support."""

    email: str
    """The email address of merchant support."""


class WeChatPayPosInfo2Dict(TypedDict):
    contact_person_name: str
    email: str
