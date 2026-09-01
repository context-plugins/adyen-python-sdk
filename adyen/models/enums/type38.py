from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type38(str, Enum):
    """**molpay**"""

    MOLPAY_EBANKING_FPX_MY = "molpay_ebanking_fpx_MY"
    MOLPAY_EBANKING_TH = "molpay_ebanking_TH"

    __str__ = str.__str__


Type38OrStr: TypeAlias = Annotated[Type38 | str, open_enum_validator(Type38)]
