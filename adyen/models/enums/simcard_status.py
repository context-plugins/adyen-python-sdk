from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SimcardStatus(str, Enum):
    """Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level,
    and only for models that support cellular connectivity.

    Possible values:
    * **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal
        itself, in the **Network** settings.
    * **INVENTORY**: the SIM card is not activated. The terminal can't use cellular connectivity."""

    ACTIVATED = "ACTIVATED"
    INVENTORY = "INVENTORY"

    __str__ = str.__str__


SimcardStatusOrStr: TypeAlias = Annotated[SimcardStatus | str, open_enum_validator(SimcardStatus)]
