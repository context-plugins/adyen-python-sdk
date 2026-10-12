from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reversal_reason1 import ReversalReason1OrStr
from .original_poitransaction2 import OriginalPoitransaction2, OriginalPoitransaction2Dict
from .sale_data import SaleData, SaleDataDict


class ReversalRequest2(SdkBaseModel):
    """Content of the Reversal Request message."""

    sale_data: Optional[SaleData] = Field(default=UNSET, alias="SaleData")
    """Data associated with the Sale System, with a particular value during the processing of the payment by the POI,
    including the cards acquisition."""

    original_poi_transaction: OriginalPoitransaction2 = Field(alias="OriginalPOITransaction")
    """Identification of a previous POI transaction."""

    reversed_amount: Optional[float] = Field(default=UNSET, alias="ReversedAmount")
    """Amount of the payment or loyalty to reverse. ReversedAmount is implicitly equal to the AuthorizedAmount if
    absent."""

    reversal_reason: ReversalReason1OrStr = Field(alias="ReversalReason")
    """Reason of the payment or loyalty reversal. Possible values:
    * **CustCancel**
    * **Malfunction**
    * **MerchantCancel**
    * **Unable2Compl**"""


class ReversalRequest2Dict(TypedDict):
    sale_data: NotRequired[SaleDataDict]
    original_poi_transaction: OriginalPoitransaction2Dict
    reversed_amount: NotRequired[float]
    reversal_reason: ReversalReason1OrStr
