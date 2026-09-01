from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sca_entity_type4 import ScaEntityType4OrStr


class ScaEntity(SdkBaseModel):
    id: str
    """The unique identifier of the entity."""

    type_: ScaEntityType4OrStr = Field(alias="type")
    """The type of the entity that you are associating with the SCA device.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""


class ScaEntityDict(TypedDict):
    id: str
    type_: ScaEntityType4OrStr
