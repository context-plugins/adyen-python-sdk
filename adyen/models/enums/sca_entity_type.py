from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaEntityType(str, Enum):
    ACCOUNT_HOLDER = "accountHolder"
    LEGAL_ENTITY = "legalEntity"
    PAYMENT_INSTRUMENT = "paymentInstrument"

    __str__ = str.__str__


ScaEntityTypeOrStr: TypeAlias = Annotated[ScaEntityType | str, open_enum_validator(ScaEntityType)]
