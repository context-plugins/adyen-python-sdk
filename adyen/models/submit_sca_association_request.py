from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sca_entity import ScaEntity, ScaEntityDict


class SubmitScaAssociationRequest(SdkBaseModel):
    entities: list[ScaEntity]
    """The list of entities to be associated."""


class SubmitScaAssociationRequestDict(TypedDict):
    entities: list[ScaEntityDict]
