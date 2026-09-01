from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address11 import Address11, Address11Dict


class BillingEntity1(SdkBaseModel):
    """The details of the entity that the order is billed to."""

    address: Optional[Address11] = UNSET
    """The address details of the billing entity."""

    email: Optional[str] = UNSET
    """The email address of the billing entity."""

    id: Optional[str] = UNSET
    """The unique identifier of the billing entity, for use as ``billingEntityId`` when creating an order."""

    name: Optional[str] = UNSET
    """The unique name of the billing entity."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax number of the billing entity."""


class BillingEntity1Dict(TypedDict):
    address: NotRequired[Address11 | Address11Dict]
    email: NotRequired[str]
    id: NotRequired[str]
    name: NotRequired[str]
    tax_id: NotRequired[str]
