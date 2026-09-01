from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.association_status1 import AssociationStatus1OrStr
from .enums.sca_entity_type2 import ScaEntityType2OrStr


class ApproveAssociationRequest(SdkBaseModel):
    entity_id: str = Field(alias="entityId")
    """The unique identifier of the entity."""

    entity_type: ScaEntityType2OrStr = Field(alias="entityType")
    """The type of the entity.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    sca_device_ids: list[str] = Field(alias="scaDeviceIds")
    """List of device ids associated to the entity that will be approved."""

    status: AssociationStatus1OrStr
    """The status of the association.

    Possible values: **active** or **pendingApproval**."""


class ApproveAssociationRequestDict(TypedDict):
    entity_id: str
    entity_type: ScaEntityType2OrStr
    sca_device_ids: list[str]
    status: AssociationStatus1OrStr
