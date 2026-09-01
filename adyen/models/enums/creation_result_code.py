from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreationResultCode(str, Enum):
    """Notification message. It informs about the outcome of the operation. Possible values:
    * CREATED
    * ALREADY_EXISTS
    * ERROR"""

    ALREADY_EXISTS = "ALREADY_EXISTS"
    CREATED = "CREATED"
    ERROR = "ERROR"

    __str__ = str.__str__


CreationResultCodeOrStr: TypeAlias = Annotated[CreationResultCode | str, open_enum_validator(CreationResultCode)]
