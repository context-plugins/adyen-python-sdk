from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReversalReason1(str, Enum):
    """Reason of the payment or loyalty reversal. Possible values:
    * **CustCancel**
    * **Malfunction**
    * **MerchantCancel**
    * **Unable2Compl**"""

    CUST_CANCEL = "CustCancel"
    MERCHANT_CANCEL = "MerchantCancel"
    MALFUNCTION = "Malfunction"
    UNABLE2_COMPL = "Unable2Compl"

    __str__ = str.__str__


ReversalReason1OrStr: TypeAlias = Annotated[ReversalReason1 | str, open_enum_validator(ReversalReason1)]
