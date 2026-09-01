from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.association_status1 import AssociationStatus1OrStr
from .enums.sca_entity_type1 import ScaEntityType1OrStr


class Association(SdkBaseModel):
    entity_id: str = Field(alias="entityId")
    """The unique identifier of the entity."""

    entity_type: ScaEntityType1OrStr = Field(alias="entityType")
    """The type of entity you are associating the device with.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    sca_device_id: str = Field(alias="scaDeviceId")
    """The unique identifier for the SCA device."""

    status: AssociationStatus1OrStr
    """The status of the association.

    Possible values: **active** or **pendingApproval**."""


class AssociationDict(TypedDict):
    entity_id: str
    entity_type: ScaEntityType1OrStr
    sca_device_id: str
    status: AssociationStatus1OrStr
