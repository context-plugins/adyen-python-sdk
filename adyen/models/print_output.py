from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.document_qualifier2 import DocumentQualifier2OrStr
from .enums.response_mode1 import ResponseMode1OrStr
from .output_content3 import OutputContent3, OutputContent3Dict


class PrintOutput(SdkBaseModel):
    document_qualifier: DocumentQualifier2OrStr = Field(alias="DocumentQualifier")
    """Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or
    POI Terminal, to send information to a physical printer or to use the paper type accordingly. Possible values:
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Journal**
    * **SaleReceipt**
    * **Voucher**"""

    response_mode: ResponseMode1OrStr = Field(alias="ResponseMode")
    """Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests
    for Print or Sound. Possible values:
    * **Immediate**
    * **NotRequired**
    * **PrintEnd**
    * **SoundEnd**"""

    integrated_print_flag: bool = Field(default=False, alias="IntegratedPrintFlag")
    """Type of the print integrated in other prints. Allows a separated printing (paper cut if available), or
    integration with the sale receipt or other print. If the printing is integrated, the response is always immediate,
    even if the ``ResponseMode`` is set to ``PrintEnd``."""

    required_signature_flag: bool = Field(default=False, alias="RequiredSignatureFlag")
    """Indicates that the cardholder payment receipt requires a physical signature by the Customer."""

    output_content: OutputContent3 = Field(alias="OutputContent")
    """Content to display or print. This is a sequence of elements if they have different formats."""


class PrintOutputDict(TypedDict):
    document_qualifier: DocumentQualifier2OrStr
    response_mode: ResponseMode1OrStr
    integrated_print_flag: NotRequired[bool]
    required_signature_flag: NotRequired[bool]
    output_content: OutputContent3Dict
