from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .device_info1 import DeviceInfo1, DeviceInfo1Dict
from .enums.status91 import Status91OrStr
from .item import Item, ItemDict


class NetworkToken2(SdkBaseModel):
    """The details of the network token."""

    brand_variant: Optional[str] = Field(default=UNSET, alias="brandVariant")
    """The card brand variant of the payment instrument associated with the network token. For example,
    **mc_prepaid_mrw**."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """Date and time when the network token was created, in `ISO 8601
    <https://www.iso.org/iso-8601-date-and-time-format.html>`__ extended format. For example,
    **2025-03-19T10:15:30+01:00**.."""

    device: Optional[DeviceInfo1] = UNSET
    """Contains information about the device used to provision the network token."""

    id: Optional[str] = UNSET
    """The unique identifier of the network token."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument to which this network token belongs to."""

    status: Optional[Status91OrStr] = UNSET
    """The status of the network token. Possible values: **active**, **inactive**, **suspended**, **closed**."""

    token_last_four: Optional[str] = Field(default=UNSET, alias="tokenLastFour")
    """The last four digits of the network token ``id``."""

    token_requestor: Optional[Item] = Field(default=UNSET, alias="tokenRequestor")
    """The token requestor is an entity who requested tokenization of the card for secure payments."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of network token. For example, **wallet**, **cof**."""


class NetworkToken2Dict(TypedDict):
    brand_variant: NotRequired[str]
    creation_date: NotRequired[RFC3339DateTime]
    device: NotRequired[DeviceInfo1Dict]
    id: NotRequired[str]
    payment_instrument_id: NotRequired[str]
    status: NotRequired[Status91OrStr]
    token_last_four: NotRequired[str]
    token_requestor: NotRequired[ItemDict]
    type_: NotRequired[str]
