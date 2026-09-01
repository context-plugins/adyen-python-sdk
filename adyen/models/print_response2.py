from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.document_qualifier2 import DocumentQualifier2OrStr
from .response11 import Response11, Response11Dict


class PrintResponse2(SdkBaseModel):
    """Content of the Print Response message."""

    document_qualifier: DocumentQualifier2OrStr = Field(alias="DocumentQualifier")
    """Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or
    POI Terminal, to send information to a physical printer or to use the paper type accordingly. Possible values:
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Journal**
    * **SaleReceipt**
    * **Voucher**"""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class PrintResponse2Dict(TypedDict):
    document_qualifier: DocumentQualifier2OrStr
    response: Response11 | Response11Dict
