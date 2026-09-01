from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SofortResponseInfo(SdkBaseModel):
    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """Sofort currency code. For example, **EUR**."""

    logo: Optional[str] = UNSET
    """Sofort logo. Format: Base64-encoded string."""


class SofortResponseInfoDict(TypedDict):
    currency_code: NotRequired[str]
    logo: NotRequired[str]
