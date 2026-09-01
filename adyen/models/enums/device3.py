from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Device3(str, Enum):
    """Logical device located on a Sale Terminal or a POI Terminal, in term of class of information to output (display,
    print or store), or input (keyboard) for the Cashier or the Customer. Copy. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    CASHIER_DISPLAY = "CashierDisplay"
    CUSTOMER_DISPLAY = "CustomerDisplay"
    CASHIER_INPUT = "CashierInput"
    CUSTOMER_INPUT = "CustomerInput"

    __str__ = str.__str__


Device3OrStr: TypeAlias = Annotated[Device3 | str, open_enum_validator(Device3)]
