from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InfoQualify3(str, Enum):
    """Qualification of the information to sent to an output logical device, to display or print to the Cashier or the
    Customer. Copy. Possible values:
    * **CustomerAssistance**
    * **Display**
    * **Document**
    * **Error**
    * **Input**
    * **POIReplication**
    * **Receipt**
    * **Sound**
    * **Status**
    * **Voucher**"""

    STATUS = "Status"
    ERROR = "Error"
    DISPLAY = "Display"
    SOUND = "Sound"
    INPUT = "Input"
    POI_REPLICATION = "POIReplication"
    CUSTOMER_ASSISTANCE = "CustomerAssistance"
    RECEIPT = "Receipt"
    DOCUMENT = "Document"
    VOUCHER = "Voucher"

    __str__ = str.__str__


InfoQualify3OrStr: TypeAlias = Annotated[InfoQualify3 | str, open_enum_validator(InfoQualify3)]
