from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestType(str, Enum):
    """Indicates the type of request to which the rule applies. If not provided, by default, this is set to
    **authorization**.

    Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**."""

    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    BANK_TRANSFER = "bankTransfer"
    TOKENIZATION = "tokenization"

    __str__ = str.__str__


RequestTypeOrStr: TypeAlias = Annotated[RequestType | str, open_enum_validator(RequestType)]
