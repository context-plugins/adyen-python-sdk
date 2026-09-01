from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InfoQualify2(str, Enum):
    """Qualification of the information to send to an output logical device, to display or print to the Cashier or the
    Customer. Possible values:
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


InfoQualify2OrStr: TypeAlias = Annotated[InfoQualify2 | str, open_enum_validator(InfoQualify2)]
