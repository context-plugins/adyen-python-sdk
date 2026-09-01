from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OrderItem(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the product."""

    installments: Optional[int] = UNSET
    """The number of installments for the specified product ``id``."""

    name: Optional[str] = UNSET
    """The name of the product."""

    quantity: Optional[int] = UNSET
    """The number of items with the specified product ``id`` included in the order."""


class OrderItemDict(TypedDict):
    id: NotRequired[str]
    installments: NotRequired[int]
    name: NotRequired[str]
    quantity: NotRequired[int]
