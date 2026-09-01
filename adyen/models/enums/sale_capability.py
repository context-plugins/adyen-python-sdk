from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SaleCapability(str, Enum):
    CASHIER_STATUS = "CashierStatus"
    CASHIER_ERROR = "CashierError"
    CASHIER_DISPLAY = "CashierDisplay"
    POI_REPLICATION = "POIReplication"
    CASHIER_INPUT = "CashierInput"
    CUSTOMER_ASSISTANCE = "CustomerAssistance"
    CUSTOMER_DISPLAY = "CustomerDisplay"
    CUSTOMER_ERROR = "CustomerError"
    CUSTOMER_INPUT = "CustomerInput"
    PRINTER_RECEIPT = "PrinterReceipt"
    PRINTER_DOCUMENT = "PrinterDocument"
    PRINTER_VOUCHER = "PrinterVoucher"
    MAG_STRIPE = "MagStripe"
    ICC = "ICC"
    EMV_CONTACTLESS = "EMVContactless"

    __str__ = str.__str__


SaleCapabilityOrStr: TypeAlias = Annotated[SaleCapability | str, open_enum_validator(SaleCapability)]
