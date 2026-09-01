from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdjustAuthType(str, Enum):
    """The type of adjustment. Possible values:

    * **cardholderInitiatedTransaction**

    * **merchantInitiatedTransaction**"""

    CARDHOLDER_INITIATED_TRANSACTION = "cardholderInitiatedTransaction"
    MERCHANT_INITIATED_TRANSACTION = "merchantInitiatedTransaction"

    __str__ = str.__str__


AdjustAuthTypeOrStr: TypeAlias = Annotated[AdjustAuthType | str, open_enum_validator(AdjustAuthType)]
