from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SofortInfo(SdkBaseModel):
    currency_code: str = Field(alias="currencyCode")
    """Sofort currency code. For example, **EUR**."""

    logo: str
    """Sofort logo. Format: Base64-encoded string."""


class SofortInfoDict(TypedDict):
    currency_code: str
    logo: str
