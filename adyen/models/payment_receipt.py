from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.document_qualifier1 import DocumentQualifier1OrStr
from .output_content1 import OutputContent1, OutputContent1Dict


class PaymentReceipt(SdkBaseModel):
    """Customer or Merchant payment receipt. If the payment receipts are printed by the Sale system and the POI or the
    Sale does not implement the Print exchange (Basic profile)."""

    document_qualifier: DocumentQualifier1OrStr = Field(alias="DocumentQualifier")
    """Qualification of the document to print to the Cashier or the Customer. SaleReceipt or CashierReceipt. Possible
    values:
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Journal**
    * **SaleReceipt**
    * **Voucher**"""

    integrated_print_flag: Optional[bool] = Field(default=UNSET, alias="IntegratedPrintFlag")
    """Type of the print integrated to other prints."""

    required_signature_flag: Optional[bool] = Field(default=UNSET, alias="RequiredSignatureFlag")
    """Indicate that the cardholder payment receipt requires a physical signature by the Customer."""

    output_content: OutputContent1 = Field(alias="OutputContent")
    """Content to display or print."""


class PaymentReceiptDict(TypedDict):
    document_qualifier: DocumentQualifier1OrStr
    integrated_print_flag: NotRequired[bool]
    required_signature_flag: NotRequired[bool]
    output_content: OutputContent1 | OutputContent1Dict
