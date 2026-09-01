from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentQualifier2(str, Enum):
    """Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or
    POI Terminal, to send information to a physical printer or to use the paper type accordingly. Possible values:
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Journal**
    * **SaleReceipt**
    * **Voucher**"""

    SALE_RECEIPT = "SaleReceipt"
    CASHIER_RECEIPT = "CashierReceipt"
    CUSTOMER_RECEIPT = "CustomerReceipt"
    DOCUMENT = "Document"
    VOUCHER = "Voucher"
    JOURNAL = "Journal"

    __str__ = str.__str__


DocumentQualifier2OrStr: TypeAlias = Annotated[DocumentQualifier2 | str, open_enum_validator(DocumentQualifier2)]
