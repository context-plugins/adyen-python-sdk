from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .defense_reason import DefenseReason, DefenseReasonDict
from .dispute_service_result1 import DisputeServiceResult1, DisputeServiceResult1Dict


class DefenseReasonsResponse(SdkBaseModel):
    defense_reasons: Optional[list[DefenseReason]] = Field(default=UNSET, alias="defenseReasons")
    """The defense reasons that can be used to defend the dispute."""

    dispute_service_result: DisputeServiceResult1 = Field(alias="disputeServiceResult")
    """The result of the dispute service."""


class DefenseReasonsResponseDict(TypedDict):
    defense_reasons: NotRequired[list[DefenseReason | DefenseReasonDict]]
    dispute_service_result: DisputeServiceResult1 | DisputeServiceResult1Dict
