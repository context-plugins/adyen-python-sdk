from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dispute_service_result1 import DisputeServiceResult1, DisputeServiceResult1Dict


class DeleteDefenseDocumentResponse(SdkBaseModel):
    dispute_service_result: DisputeServiceResult1 = Field(alias="disputeServiceResult")
    """The result of the dispute service."""


class DeleteDefenseDocumentResponseDict(TypedDict):
    dispute_service_result: DisputeServiceResult1Dict
