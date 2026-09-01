from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaEntityType1(str, Enum):
    """The type of entity you are associating the device with.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    ACCOUNT_HOLDER = "accountHolder"
    LEGAL_ENTITY = "legalEntity"
    PAYMENT_INSTRUMENT = "paymentInstrument"

    __str__ = str.__str__


ScaEntityType1OrStr: TypeAlias = Annotated[ScaEntityType1 | str, open_enum_validator(ScaEntityType1)]
