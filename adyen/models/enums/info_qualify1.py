from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InfoQualify1(str, Enum):
    """Qualification of the information to sent to an output logical device, to display or print to the Cashier or the
    Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical
    device or to present the information accordingly. Possible values:
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


InfoQualify1OrStr: TypeAlias = Annotated[InfoQualify1 | str, open_enum_validator(InfoQualify1)]
