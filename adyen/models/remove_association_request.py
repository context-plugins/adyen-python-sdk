from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sca_entity_type3 import ScaEntityType3OrStr


class RemoveAssociationRequest(SdkBaseModel):
    entity_id: str = Field(alias="entityId")
    """The unique identifier of the entity."""

    entity_type: ScaEntityType3OrStr = Field(alias="entityType")
    """The type of the entity.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    sca_device_ids: list[str] = Field(alias="scaDeviceIds")
    """A list of device ids associated with the entity that should be removed."""


class RemoveAssociationRequestDict(TypedDict):
    entity_id: str
    entity_type: ScaEntityType3OrStr
    sca_device_ids: list[str]
