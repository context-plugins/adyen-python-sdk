from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SofortResponseInfo2(SdkBaseModel):
    """Sofort details."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """Sofort currency code. For example, **EUR**."""

    logo: Optional[str] = UNSET
    """Sofort logo. Format: Base64-encoded string."""


class SofortResponseInfo2Dict(TypedDict):
    currency_code: NotRequired[str]
    logo: NotRequired[str]
