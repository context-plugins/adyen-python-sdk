from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaEntityType3(str, Enum):
    """The type of the entity.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    ACCOUNT_HOLDER = "accountHolder"
    LEGAL_ENTITY = "legalEntity"
    PAYMENT_INSTRUMENT = "paymentInstrument"

    __str__ = str.__str__


ScaEntityType3OrStr: TypeAlias = Annotated[ScaEntityType3 | str, open_enum_validator(ScaEntityType3)]
