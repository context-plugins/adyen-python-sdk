from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..interchange_data import InterchangeData, InterchangeDataDict
from ..issuing_transaction_data import IssuingTransactionData, IssuingTransactionDataDict
from ..merchant_purchase_data import MerchantPurchaseData, MerchantPurchaseDataDict

EventsDatum: TypeAlias = Annotated[
    InterchangeData | IssuingTransactionData | MerchantPurchaseData, Field(discriminator="type_")
]

EventsDatumDict: TypeAlias = InterchangeDataDict | IssuingTransactionDataDict | MerchantPurchaseDataDict
