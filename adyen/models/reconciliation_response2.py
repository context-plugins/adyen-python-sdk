from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reconciliation_type1 import ReconciliationType1OrStr
from .response11 import Response11, Response11Dict
from .transaction_totals import TransactionTotals, TransactionTotalsDict


class ReconciliationResponse2(SdkBaseModel):
    """Content of the Reconciliation Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    reconciliation_type: ReconciliationType1OrStr = Field(alias="ReconciliationType")
    """Type of Reconciliation requested by the Sale to the POI. Possible values:
    * **AcquirerReconciliation**
    * **AcquirerSynchronisation**
    * **PreviousReconciliation**
    * **SaleReconciliation**"""

    poi_reconciliation_id: Optional[int] = Field(default=UNSET, alias="POIReconciliationID")
    """Identification of the reconciliation period between Sale and POI. Absent if ReconciliationType is
    ``AcquirerReconciliation``."""

    transaction_totals: Optional[list[TransactionTotals]] = Field(default=UNSET, alias="TransactionTotals")
    """Result of the Sale to POI Reconciliation processing. If ``Response.Result`` is Success."""


class ReconciliationResponse2Dict(TypedDict):
    response: Response11Dict
    reconciliation_type: ReconciliationType1OrStr
    poi_reconciliation_id: NotRequired[int]
    transaction_totals: NotRequired[list[TransactionTotalsDict]]
