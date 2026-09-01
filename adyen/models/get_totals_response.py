from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response11 import Response11, Response11Dict
from .transaction_totals import TransactionTotals, TransactionTotalsDict


class GetTotalsResponse(SdkBaseModel):
    """Content of the Reconciliation Response message. It conveys Information related to the Reconciliation transaction
    processed by the POI System."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    poi_reconciliation_id: int = Field(alias="POIReconciliationID")
    """Identification of the reconciliation period between Sale and POI."""

    transaction_totals: Optional[list[TransactionTotals]] = Field(default=UNSET, alias="TransactionTotals")
    """Result of the Sale to POI Reconciliation processing. If ``Response.Result`` is Success."""


class GetTotalsResponseDict(TypedDict):
    response: Response11 | Response11Dict
    poi_reconciliation_id: int
    transaction_totals: NotRequired[list[TransactionTotals | TransactionTotalsDict]]
