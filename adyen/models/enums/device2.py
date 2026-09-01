from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Device2(str, Enum):
    """Logical device located on a Sale Terminal or a POI Terminal, regarding the class of information to output
    (display, print or store), or input (keyboard) for the Cashier or the Customer. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    CASHIER_DISPLAY = "CashierDisplay"
    CUSTOMER_DISPLAY = "CustomerDisplay"
    CASHIER_INPUT = "CashierInput"
    CUSTOMER_INPUT = "CustomerInput"

    __str__ = str.__str__


Device2OrStr: TypeAlias = Annotated[Device2 | str, open_enum_validator(Device2)]
