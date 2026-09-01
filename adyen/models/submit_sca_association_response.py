from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .association import Association, AssociationDict


class SubmitScaAssociationResponse(SdkBaseModel):
    sca_associations: list[Association] = Field(alias="scaAssociations")
    """List of associations created to the entities and their statuses."""


class SubmitScaAssociationResponseDict(TypedDict):
    sca_associations: list[Association | AssociationDict]
