from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status2(str, Enum):
    """The status of your request.

    If you included ``adjustAuthorisationData`` in your request, possible values are the following:

    * **authorised**

    * **refused**

    Otherwise, the value is **received**."""

    AUTHORISED = "authorised"
    RECEIVED = "received"
    REFUSED = "refused"

    __str__ = str.__str__


Status2OrStr: TypeAlias = Annotated[Status2 | str, open_enum_validator(Status2)]
