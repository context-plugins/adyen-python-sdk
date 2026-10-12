from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.customer_order_req import CustomerOrderReqOrStr
from .enums.token_requested_type1 import TokenRequestedType1OrStr
from .sale_terminal_data1 import SaleTerminalData1, SaleTerminalData1Dict
from .sale_to_issuer_data1 import SaleToIssuerData1, SaleToIssuerData1Dict
from .transaction_idtype1 import TransactionIdtype1, TransactionIdtype1Dict


class SaleData(SdkBaseModel):
    """Data associated with the Sale System, with a particular value during the processing of the payment by the POI,
    including the cards acquisition."""

    operator_id: Optional[str] = Field(default=UNSET, alias="OperatorID")
    """Identification of the Cashier or Operator."""

    operator_language: Optional[str] = Field(default=UNSET, alias="OperatorLanguage")
    """Language of the Cashier or Operator. If different from the Login."""

    shift_number: Optional[str] = Field(default=UNSET, alias="ShiftNumber")
    """Shift number. If different from the Login, see Login SaleData."""

    sale_transaction_id: TransactionIdtype1 = Field(alias="SaleTransactionID")
    """Identification of a Sale transaction."""

    sale_reference_id: Optional[str] = Field(default=UNSET, alias="SaleReferenceID")
    """Identification of a Sale global transaction for a sequence of related POI transactions. If payment
    reservation."""

    sale_terminal_data: Optional[SaleTerminalData1] = Field(default=UNSET, alias="SaleTerminalData")
    """Information related to the software and hardware features of the Sale Terminal. If content is not empty."""

    token_requested_type: Optional[TokenRequestedType1OrStr] = Field(default=UNSET, alias="TokenRequestedType")
    """Type of token replacing the PAN of a payment card to identify the payment
     mean of the customer. It allows, for a merchant, to use a token for a transaction
     only or for a longer period.
    Possible values:
    * **Customer**
    * **Transaction**"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="CustomerOrderID")
    """Additional and optional identification of a customer order."""

    customer_order_req: Optional[list[CustomerOrderReqOrStr]] = Field(default=UNSET, alias="CustomerOrderReq")
    """List of customer order open, closed or both to be sent in the response messages. Possible values:
    * **Both**
    * **Closed**
    * **Open**"""

    sale_to_poi_data: Optional[str] = Field(default=UNSET, alias="SaleToPOIData")
    """Sale information intended for the POI. Stored with the transaction."""

    sale_to_acquirer_data: Optional[str] = Field(default=UNSET, alias="SaleToAcquirerData")
    """Sale information intended for the Acquirer. Send to the Acquirer if present."""

    sale_to_issuer_data: Optional[SaleToIssuerData1] = Field(default=UNSET, alias="SaleToIssuerData")
    """Sale information intended for the Issuer. Send to the Acquirer if present."""


class SaleDataDict(TypedDict):
    operator_id: NotRequired[str]
    operator_language: NotRequired[str]
    shift_number: NotRequired[str]
    sale_transaction_id: TransactionIdtype1Dict
    sale_reference_id: NotRequired[str]
    sale_terminal_data: NotRequired[SaleTerminalData1Dict]
    token_requested_type: NotRequired[TokenRequestedType1OrStr]
    customer_order_id: NotRequired[str]
    customer_order_req: NotRequired[list[CustomerOrderReqOrStr]]
    sale_to_poi_data: NotRequired[str]
    sale_to_acquirer_data: NotRequired[str]
    sale_to_issuer_data: NotRequired[SaleToIssuerData1Dict]
