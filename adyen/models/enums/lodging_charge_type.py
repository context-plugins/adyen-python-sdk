from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LodgingChargeType(str, Enum):
    """The category of lodging charges for the payment.
    * **additionalData key:** ``lodging.specialProgramCode``"""

    ADVANCE_DEPOSIT = "advanceDeposit"
    NO_SHOW = "noShow"
    STAY = "stay"

    __str__ = str.__str__


LodgingChargeTypeOrStr: TypeAlias = Annotated[LodgingChargeType | str, open_enum_validator(LodgingChargeType)]
