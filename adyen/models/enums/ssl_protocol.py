from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SslProtocol(str, Enum):
    """The SSL protocol employed by the endpoint. >Permitted values: ``TLSv12``, ``TLSv13``."""

    TL_SV12 = "TLSv12"
    TL_SV13 = "TLSv13"

    __str__ = str.__str__


SslProtocolOrStr: TypeAlias = Annotated[SslProtocol | str, open_enum_validator(SslProtocol)]
