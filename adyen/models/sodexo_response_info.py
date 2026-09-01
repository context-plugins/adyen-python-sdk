from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SodexoResponseInfo(SdkBaseModel):
    merchant_contact_phone: Optional[str] = Field(default=UNSET, alias="merchantContactPhone")
    """Sodexo merchantContactPhone"""


class SodexoResponseInfoDict(TypedDict):
    merchant_contact_phone: NotRequired[str]
