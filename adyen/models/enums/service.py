from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Service(str, Enum):
    """The service for which you are creating the business line.



    Possible values:
    * **paymentProcessing**
    * **issuing**
    * **banking**"""

    PAYMENT_PROCESSING = "paymentProcessing"
    ISSUING = "issuing"
    BANKING = "banking"

    __str__ = str.__str__


ServiceOrStr: TypeAlias = Annotated[Service | str, open_enum_validator(Service)]
