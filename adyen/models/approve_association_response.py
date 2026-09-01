from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .association import Association, AssociationDict


class ApproveAssociationResponse(SdkBaseModel):
    sca_associations: list[Association] = Field(alias="scaAssociations")
    """The list of associations."""


class ApproveAssociationResponseDict(TypedDict):
    sca_associations: list[Association | AssociationDict]
