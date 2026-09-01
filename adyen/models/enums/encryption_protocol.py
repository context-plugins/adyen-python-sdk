from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EncryptionProtocol(str, Enum):
    """SSL version to access the public webhook URL specified in the ``url`` field. Possible values:
    * **TLSv1.3**
    * **TLSv1.2**
    * **HTTP** - Only allowed on Test environment.

    If not specified, the webhook will use ``sslVersion``: **TLSv1.2**."""

    HTTP = "HTTP"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"

    __str__ = str.__str__


EncryptionProtocolOrStr: TypeAlias = Annotated[EncryptionProtocol | str, open_enum_validator(EncryptionProtocol)]
