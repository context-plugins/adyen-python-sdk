from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type56(str, Enum):
    """**wechatpay**"""

    WECHATPAY = "wechatpay"
    WECHATPAY_POS = "wechatpay_pos"

    __str__ = str.__str__


Type56OrStr: TypeAlias = Annotated[Type56 | str, open_enum_validator(Type56)]
