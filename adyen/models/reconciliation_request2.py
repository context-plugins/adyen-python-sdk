from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reconciliation_type1 import ReconciliationType1OrStr


class ReconciliationRequest2(SdkBaseModel):
    """Content of the Reconciliation Request message."""

    reconciliation_type: ReconciliationType1OrStr = Field(alias="ReconciliationType")
    """Type of Reconciliation requested by the Sale to the POI. Possible values:
    * **AcquirerReconciliation**
    * **AcquirerSynchronisation**
    * **PreviousReconciliation**
    * **SaleReconciliation**"""

    acquirer_id: Optional[list[int]] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer. Could be present only if ReconciliationType is AcquirerReconciliation or
    AcquirerSynchronisation."""

    poi_reconciliation_id: Optional[int] = Field(default=UNSET, alias="POIReconciliationID")
    """Identification of the reconciliation period between Sale and POI. Absent if ReconciliationType is not
    PreviousReconciliation."""


class ReconciliationRequest2Dict(TypedDict):
    reconciliation_type: ReconciliationType1OrStr
    acquirer_id: NotRequired[list[int]]
    poi_reconciliation_id: NotRequired[int]
