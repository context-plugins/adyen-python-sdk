from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.association_status1 import AssociationStatus1OrStr
from .enums.sca_device_type3 import ScaDeviceType3OrStr
from .enums.sca_entity_type2 import ScaEntityType2OrStr


class AssociationListing(SdkBaseModel):
    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The date and time when the association was created."""

    entity_id: str = Field(alias="entityId")
    """The unique identifier of the entity."""

    entity_type: ScaEntityType2OrStr = Field(alias="entityType")
    """The type of the entity.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    sca_device_id: str = Field(alias="scaDeviceId")
    """The unique identifier of the SCA device."""

    sca_device_name: Optional[str] = Field(default=UNSET, alias="scaDeviceName")
    """The human-readable name for the SCA device that was registered."""

    sca_device_type: ScaDeviceType3OrStr = Field(alias="scaDeviceType")
    """The type of the device."""

    status: AssociationStatus1OrStr
    """The status of the association.

    Possible values: **active** or **pendingApproval**."""


class AssociationListingDict(TypedDict):
    created_at: RFC3339DateTime
    entity_id: str
    entity_type: ScaEntityType2OrStr
    sca_device_id: str
    sca_device_name: NotRequired[str]
    sca_device_type: ScaDeviceType3OrStr
    status: AssociationStatus1OrStr
