from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address21 import Address21, Address21Dict
from .contact1 import Contact1, Contact1Dict


class ShippingLocation1(SdkBaseModel):
    """The details of the location where the order is shipped to."""

    address: Optional[Address21] = UNSET
    """The address details of the shipping location."""

    contact: Optional[Contact1] = UNSET
    """The contact details for the shipping location."""

    id: Optional[str] = UNSET
    """The unique identifier of the shipping location, for use as ``shippingLocationId`` when creating an order."""

    name: Optional[str] = UNSET
    """The unique name of the shipping location."""


class ShippingLocation1Dict(TypedDict):
    address: NotRequired[Address21 | Address21Dict]
    contact: NotRequired[Contact1 | Contact1Dict]
    id: NotRequired[str]
    name: NotRequired[str]
