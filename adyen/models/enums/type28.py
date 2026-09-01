from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type28(str, Enum):
    """**dragonpay**"""

    DRAGONPAY_EBANKING = "dragonpay_ebanking"
    DRAGONPAY_OTC_BANKING = "dragonpay_otc_banking"
    DRAGONPAY_OTC_NON_BANKING = "dragonpay_otc_non_banking"
    DRAGONPAY_OTC_PHILIPPINES = "dragonpay_otc_philippines"

    __str__ = str.__str__


Type28OrStr: TypeAlias = Annotated[Type28 | str, open_enum_validator(Type28)]
