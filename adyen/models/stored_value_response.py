from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_receipt import PaymentReceipt, PaymentReceiptDict
from .poidata1 import Poidata1, Poidata1Dict
from .response11 import Response11, Response11Dict
from .sale_data1 import SaleData1, SaleData1Dict
from .stored_value_result import StoredValueResult, StoredValueResultDict


class StoredValueResponse(SdkBaseModel):
    """It conveys Information related to the Stored Value transaction processed by the POI System. Content of the Stored
    Value Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    poi_data: Poidata1 = Field(alias="POIData")
    """Data related to the POI System."""

    stored_value_result: Optional[list[StoredValueResult]] = Field(default=UNSET, alias="StoredValueResult")
    """Result of loading/reloading a stored value card. If StoredValueResponse.Result is Success or Partial, one entry
    per StoredValueRequest.StoredValueData loaded or activated."""

    payment_receipt: Optional[list[PaymentReceipt]] = Field(default=UNSET, alias="PaymentReceipt")


class StoredValueResponseDict(TypedDict):
    response: Response11 | Response11Dict
    sale_data: SaleData1 | SaleData1Dict
    poi_data: Poidata1 | Poidata1Dict
    stored_value_result: NotRequired[list[StoredValueResult | StoredValueResultDict]]
    payment_receipt: NotRequired[list[PaymentReceipt | PaymentReceiptDict]]
