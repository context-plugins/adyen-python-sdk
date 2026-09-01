from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SodexoInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **sodexo**."""

    merchant_contact_phone: str = Field(alias="merchantContactPhone")
    """Sodexo merchantContactPhone"""


class SodexoInfo2Dict(TypedDict):
    merchant_contact_phone: str
