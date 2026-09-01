from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type14(str, Enum):
    """Default payment method details. Common for scheme payment methods, and for simple payment method details."""

    BCMC = "bcmc"
    SCHEME = "scheme"
    NETWORK_TOKEN = "networkToken"
    GIFTCARD = "giftcard"
    CARD = "card"
    CLICKTOPAY = "clicktopay"

    __str__ = str.__str__


Type14OrStr: TypeAlias = Annotated[Type14 | str, open_enum_validator(Type14)]
