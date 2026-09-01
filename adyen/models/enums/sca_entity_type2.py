from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaEntityType2(str, Enum):
    """The type of the entity.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    ACCOUNT_HOLDER = "accountHolder"
    LEGAL_ENTITY = "legalEntity"
    PAYMENT_INSTRUMENT = "paymentInstrument"

    __str__ = str.__str__


ScaEntityType2OrStr: TypeAlias = Annotated[ScaEntityType2 | str, open_enum_validator(ScaEntityType2)]
