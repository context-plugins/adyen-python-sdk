from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HttpMethodModel(str, Enum):
    """The HTTP method to use for the request Adyen makes on your behalf to the third party."""

    POST = "post"
    PUT = "put"
    PATCH = "patch"

    __str__ = str.__str__


HttpMethodModelOrStr: TypeAlias = Annotated[HttpMethodModel | str, open_enum_validator(HttpMethodModel)]
