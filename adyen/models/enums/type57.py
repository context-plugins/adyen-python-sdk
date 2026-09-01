from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type57(str, Enum):
    """**wechatpayMiniProgram**"""

    WECHATPAY_MINI_PROGRAM = "wechatpayMiniProgram"

    __str__ = str.__str__


Type57OrStr: TypeAlias = Annotated[Type57 | str, open_enum_validator(Type57)]
