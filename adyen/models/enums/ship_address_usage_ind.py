from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipAddressUsageInd(str, Enum):
    """Indicates when the shipping address used for this transaction was first used with the 3DS Requestor. Allowed
    values:
    * **01** — This transaction
    * **02** — Less than 30 days
    * **03** — 30–60 days
    * **04** — More than 60 days"""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"

    __str__ = str.__str__


ShipAddressUsageIndOrStr: TypeAlias = Annotated[ShipAddressUsageInd | str, open_enum_validator(ShipAddressUsageInd)]
