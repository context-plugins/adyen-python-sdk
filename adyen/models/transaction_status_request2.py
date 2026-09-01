from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.document_qualifier import DocumentQualifierOrStr
from .message_reference2 import MessageReference2, MessageReference2Dict


class TransactionStatusRequest2(SdkBaseModel):
    """Content of the TransactionStatus Request message."""

    message_reference: Optional[MessageReference2] = Field(default=UNSET, alias="MessageReference")
    """Identification of a previous POI transaction. Present if it contains any data."""

    receipt_reprint_flag: Optional[bool] = Field(default=UNSET, alias="ReceiptReprintFlag")
    """Request to reprint the POI receipt(s). Allows reprinting a receipt with a ``TransactionStatus`` message"""

    document_qualifier: Optional[list[DocumentQualifierOrStr]] = Field(default=UNSET, alias="DocumentQualifier")
    """Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or
    POI Terminal, to send the information to a particular physical printer or to use the paper type accordingly.
    Possible values:
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Journal**
    * **SaleReceipt**
    * **Voucher**"""


class TransactionStatusRequest2Dict(TypedDict):
    message_reference: NotRequired[MessageReference2 | MessageReference2Dict]
    receipt_reprint_flag: NotRequired[bool]
    document_qualifier: NotRequired[list[DocumentQualifierOrStr]]
