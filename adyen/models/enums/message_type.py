from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageType(str, Enum):
    """Possible values:
    * **Request**
    * **Response**
    * **Notification**"""

    REQUEST = "Request"
    RESPONSE = "Response"
    NOTIFICATION = "Notification"

    __str__ = str.__str__


MessageTypeOrStr: TypeAlias = Annotated[MessageType | str, open_enum_validator(MessageType)]
