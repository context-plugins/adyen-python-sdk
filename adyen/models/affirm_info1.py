from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AffirmInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **affirm**."""

    price_plan: Optional[str] = Field(default=UNSET, alias="pricePlan")
    """Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if
    no selection made."""

    support_email: str = Field(alias="supportEmail")
    """Merchant support email used to manage disputes."""


class AffirmInfo1Dict(TypedDict):
    price_plan: NotRequired[str]
    support_email: str
