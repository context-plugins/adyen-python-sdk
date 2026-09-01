from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaEntityType4(str, Enum):
    """The type of the entity that you are associating with the SCA device.

    Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**."""

    ACCOUNT_HOLDER = "accountHolder"
    LEGAL_ENTITY = "legalEntity"
    PAYMENT_INSTRUMENT = "paymentInstrument"

    __str__ = str.__str__


ScaEntityType4OrStr: TypeAlias = Annotated[ScaEntityType4 | str, open_enum_validator(ScaEntityType4)]
