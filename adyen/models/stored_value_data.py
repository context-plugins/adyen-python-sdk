from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stored_value_transaction_type1 import StoredValueTransactionType1OrStr
from .original_poitransaction1 import OriginalPoitransaction1, OriginalPoitransaction1Dict
from .stored_value_account_id1 import StoredValueAccountId1, StoredValueAccountId1Dict


class StoredValueData(SdkBaseModel):
    """It contains: - the identification of the stored value accounts or the stored value cards, if provided by the Sale
    System, and - the associated products sold by the Sale System. Data related to the stored value card."""

    stored_value_provider: Optional[str] = Field(default=UNSET, alias="StoredValueProvider")
    """Identification of the provider of the stored value account load/reload. If more than one provider to manage on
    the POI, and StoredValueAccountID absent."""

    stored_value_transaction_type: StoredValueTransactionType1OrStr = Field(alias="StoredValueTransactionType")
    """Identification of operation to proceed on the stored value account or the stored value card. Possible values:
    * **Activate**
    * **Duplicate**
    * **Load**
    * **Reserve**
    * **Reverse**
    * **Unload**"""

    stored_value_account_id: Optional[StoredValueAccountId1] = Field(default=UNSET, alias="StoredValueAccountID")
    """Identification of the stored value account or the stored value card. If the identification of the Stored Value
    account or card has been made by the Sale System before the request."""

    original_poi_transaction: Optional[OriginalPoitransaction1] = Field(default=UNSET, alias="OriginalPOITransaction")
    """Identification of a previous POI transaction. If StoredValueTransactionType is Reverse or Duplicate."""

    product_code: Optional[int] = Field(default=UNSET, alias="ProductCode")
    """Product code of item purchased with the transaction."""

    ean_upc: Optional[int] = Field(default=UNSET, alias="EanUpc")
    """Standard product code of item purchased with the transaction."""

    item_amount: Optional[float] = Field(default=UNSET, alias="ItemAmount")
    """Total amount of the item line."""

    currency: Optional[str] = Field(default=UNSET, alias="Currency")
    """Currency of a monetary amount."""


class StoredValueDataDict(TypedDict):
    stored_value_provider: NotRequired[str]
    stored_value_transaction_type: StoredValueTransactionType1OrStr
    stored_value_account_id: NotRequired[StoredValueAccountId1 | StoredValueAccountId1Dict]
    original_poi_transaction: NotRequired[OriginalPoitransaction1 | OriginalPoitransaction1Dict]
    product_code: NotRequired[int]
    ean_upc: NotRequired[int]
    item_amount: NotRequired[float]
    currency: NotRequired[str]
