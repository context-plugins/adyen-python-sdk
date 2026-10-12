from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..interchange_data import InterchangeData, InterchangeDataDict
from ..issuing_transaction_data import IssuingTransactionData, IssuingTransactionDataDict
from ..merchant_purchase_data import MerchantPurchaseData, MerchantPurchaseDataDict

EventsDatum: TypeAlias = Annotated[
    (
        Annotated[InterchangeData, Tag("interchangeData")]
        | Annotated[IssuingTransactionData, Tag("issuingTransactionData")]
        | Annotated[MerchantPurchaseData, Tag("merchantPurchaseData")]
    ),
    WireDiscriminator("type"),
]

EventsDatumDict: TypeAlias = InterchangeDataDict | IssuingTransactionDataDict | MerchantPurchaseDataDict
