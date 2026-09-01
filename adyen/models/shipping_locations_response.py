from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipping_location import ShippingLocation, ShippingLocationDict


class ShippingLocationsResponse(SdkBaseModel):
    data: Optional[list[ShippingLocation]] = UNSET
    """Physical locations where orders can be shipped to."""


class ShippingLocationsResponseDict(TypedDict):
    data: NotRequired[list[ShippingLocation | ShippingLocationDict]]
