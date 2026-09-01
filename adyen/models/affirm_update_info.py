from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AffirmUpdateInfo(SdkBaseModel):
    price_plan: Optional[str] = Field(default=UNSET, alias="pricePlan")
    """Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if
    no selection made."""


class AffirmUpdateInfoDict(TypedDict):
    price_plan: NotRequired[str]
