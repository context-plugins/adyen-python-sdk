from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServicesEnabled(str, Enum):
    CARD_ACQUISITION = "CardAcquisition"
    PAYMENT = "Payment"
    LOYALTY = "Loyalty"

    __str__ = str.__str__


ServicesEnabledOrStr: TypeAlias = Annotated[ServicesEnabled | str, open_enum_validator(ServicesEnabled)]
