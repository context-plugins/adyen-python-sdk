from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SodexoResponseInfo2(SdkBaseModel):
    """**sodexo** details"""

    merchant_contact_phone: Optional[str] = Field(default=UNSET, alias="merchantContactPhone")
    """Sodexo merchantContactPhone"""


class SodexoResponseInfo2Dict(TypedDict):
    merchant_contact_phone: NotRequired[str]
