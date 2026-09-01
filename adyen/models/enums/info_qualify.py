from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InfoQualify(str, Enum):
    """Possible values:
    * **Status**
    * **Error**
    * **Display**
    * **Sound**
    * **Input**
    * **POIReplication**
    * **CustomerAssistance**
    * **Receipt**
    * **Document**
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


InfoQualifyOrStr: TypeAlias = Annotated[InfoQualify | str, open_enum_validator(InfoQualify)]
