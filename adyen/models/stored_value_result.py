from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stored_value_transaction_type2 import StoredValueTransactionType2OrStr
from .stored_value_account_status1 import StoredValueAccountStatus1, StoredValueAccountStatus1Dict
from .transaction_idtype7 import TransactionIdtype7, TransactionIdtype7Dict


class StoredValueResult(SdkBaseModel):
    """For each stored value card loaded or reloaded, in the StoredValue response message. Result of loading/reloading a
    stored value card."""

    stored_value_transaction_type: StoredValueTransactionType2OrStr = Field(alias="StoredValueTransactionType")
    """Identification of operation to proceed on the stored value account or the stored value card. Copy. Possible
    values:
    * **Activate**
    * **Duplicate**
    * **Load**
    * **Reserve**
    * **Reverse**
    * **Unload**"""

    product_code: Optional[int] = Field(default=UNSET, alias="ProductCode")
    """Product code of item purchased with the transaction. Copy."""

    ean_upc: Optional[int] = Field(default=UNSET, alias="EanUpc")
    """Standard product code of item purchased with the transaction. Copy."""

    item_amount: Optional[float] = Field(default=UNSET, alias="ItemAmount")
    """Total amount of the item line."""

    currency: Optional[str] = Field(default=UNSET, alias="Currency")
    """Currency of a monetary amount. Copy."""

    stored_value_account_status: Optional[StoredValueAccountStatus1] = Field(
        default=UNSET, alias="StoredValueAccountStatus"
    )
    """Data related to the result of the stored value card transaction."""

    host_transaction_id: Optional[TransactionIdtype7] = Field(default=UNSET, alias="HostTransactionID")
    """Identification of the transaction by the host in charge of the stored value transaction. If provided by the
    Host."""


class StoredValueResultDict(TypedDict):
    stored_value_transaction_type: StoredValueTransactionType2OrStr
    product_code: NotRequired[int]
    ean_upc: NotRequired[int]
    item_amount: NotRequired[float]
    currency: NotRequired[str]
    stored_value_account_status: NotRequired[StoredValueAccountStatus1Dict]
    host_transaction_id: NotRequired[TransactionIdtype7Dict]
