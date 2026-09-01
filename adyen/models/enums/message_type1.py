from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageType1(str, Enum):
    """Type of message of the Sale to POI protocol. Possible values:
    * **Notification**
    * **Request**
    * **Response**"""

    REQUEST = "Request"
    RESPONSE = "Response"
    NOTIFICATION = "Notification"

    __str__ = str.__str__


MessageType1OrStr: TypeAlias = Annotated[MessageType1 | str, open_enum_validator(MessageType1)]
