from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_entity import BillingEntity, BillingEntityDict


class BillingEntitiesResponse(SdkBaseModel):
    data: Optional[list[BillingEntity]] = UNSET
    """List of legal entities that can be used for the billing of orders."""


class BillingEntitiesResponseDict(TypedDict):
    data: NotRequired[list[BillingEntity | BillingEntityDict]]
