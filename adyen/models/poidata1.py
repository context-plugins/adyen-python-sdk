from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_idtype2 import TransactionIdtype2, TransactionIdtype2Dict


class Poidata1(SdkBaseModel):
    """Data related to the POI System."""

    poi_transaction_id: TransactionIdtype2 = Field(alias="POITransactionID")
    """Unique identification of a POI transaction for a POI."""

    poi_reconciliation_id: Optional[int] = Field(default=UNSET, alias="POIReconciliationID")
    """Identification of the reconciliation period between Sale and POI. If Result is Success."""


class Poidata1Dict(TypedDict):
    poi_transaction_id: TransactionIdtype2 | TransactionIdtype2Dict
    poi_reconciliation_id: NotRequired[int]
