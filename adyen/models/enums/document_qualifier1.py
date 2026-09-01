from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentQualifier1(str, Enum):
    """Qualification of the document to print to the Cashier or the Customer. SaleReceipt or CashierReceipt. Possible
    values:
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


DocumentQualifier1OrStr: TypeAlias = Annotated[DocumentQualifier1 | str, open_enum_validator(DocumentQualifier1)]
