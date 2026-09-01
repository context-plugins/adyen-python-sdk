from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SodexoInfo(SdkBaseModel):
    merchant_contact_phone: str = Field(alias="merchantContactPhone")
    """Sodexo merchantContactPhone"""


class SodexoInfoDict(TypedDict):
    merchant_contact_phone: str
