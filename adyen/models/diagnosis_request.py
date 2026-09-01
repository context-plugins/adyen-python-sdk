from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DiagnosisRequest(SdkBaseModel):
    """It conveys Information related to the target POI for which the diagnosis is requested. Content of the Diagnosis
    Request message."""

    poiid: Optional[str] = Field(default=UNSET, alias="POIID")
    """Identification of a POI System or a POI Terminal for the Sale to POI protocol. MessageHeader.POIID."""

    host_diagnosis_flag: Optional[bool] = Field(default=UNSET, alias="HostDiagnosisFlag")
    """Indicates if Host Diagnosis are required."""

    acquirer_id: Optional[list[int]] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer. Present if requesting the diagnosis of these hosts only."""


class DiagnosisRequestDict(TypedDict):
    poiid: NotRequired[str]
    host_diagnosis_flag: NotRequired[bool]
    acquirer_id: NotRequired[list[int]]
