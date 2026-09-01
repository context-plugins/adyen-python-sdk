from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StateType(str, Enum):
    """The state to be updated. >Permitted values are: ``Processing``, ``Payout``"""

    LIMITED_PAYOUT = "LimitedPayout"
    LIMITED_PROCESSING = "LimitedProcessing"
    LIMITLESS_PAYOUT = "LimitlessPayout"
    LIMITLESS_PROCESSING = "LimitlessProcessing"
    PAYOUT = "Payout"
    PROCESSING = "Processing"

    __str__ = str.__str__


StateTypeOrStr: TypeAlias = Annotated[StateType | str, open_enum_validator(StateType)]
