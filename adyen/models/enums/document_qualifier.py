from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentQualifier(str, Enum):
    """Possible values:
    * **SaleReceipt**
    * **CashierReceipt**
    * **CustomerReceipt**
    * **Document**
    * **Voucher**
    * **Journal**"""

    SALE_RECEIPT = "SaleReceipt"
    CASHIER_RECEIPT = "CashierReceipt"
    CUSTOMER_RECEIPT = "CustomerReceipt"
    DOCUMENT = "Document"
    VOUCHER = "Voucher"
    JOURNAL = "Journal"

    __str__ = str.__str__


DocumentQualifierOrStr: TypeAlias = Annotated[DocumentQualifier | str, open_enum_validator(DocumentQualifier)]
