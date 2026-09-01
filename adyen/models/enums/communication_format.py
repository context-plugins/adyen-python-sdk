from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommunicationFormat(str, Enum):
    """Format or protocol for receiving webhooks. Possible values:
    * **soap**
    * **http**
    * **json**"""

    HTTP = "http"
    JSON = "json"
    SOAP = "soap"

    __str__ = str.__str__


CommunicationFormatOrStr: TypeAlias = Annotated[CommunicationFormat | str, open_enum_validator(CommunicationFormat)]
