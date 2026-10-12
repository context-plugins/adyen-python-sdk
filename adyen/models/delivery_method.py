from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount24 import Amount24, Amount24Dict
from .enums.type21 import Type21OrStr


class DeliveryMethod(SdkBaseModel):
    amount: Optional[Amount24] = UNSET
    """The cost of this delivery method."""

    description: Optional[str] = UNSET
    """The name of the delivery method as shown to the shopper."""

    reference: Optional[str] = UNSET
    """The reference of the delivery method."""

    selected: Optional[bool] = UNSET
    """If you display the PayPal lightbox with delivery methods, set to **true** for the delivery method that is
    selected. Only one delivery method can be selected at a time."""

    type_: Optional[Type21OrStr] = Field(default=UNSET, alias="type")
    """The type of the delivery method."""


class DeliveryMethodDict(TypedDict):
    amount: NotRequired[Amount24Dict]
    description: NotRequired[str]
    reference: NotRequired[str]
    selected: NotRequired[bool]
    type_: NotRequired[Type21OrStr]
