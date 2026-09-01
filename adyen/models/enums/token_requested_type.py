from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TokenRequestedType(str, Enum):
    """Type of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a
    merchant, to use a token for a transaction only or for a longer period. Possible values:
    * **Transaction**
    * **Customer**"""

    TRANSACTION = "Transaction"
    CUSTOMER = "Customer"

    __str__ = str.__str__


TokenRequestedTypeOrStr: TypeAlias = Annotated[TokenRequestedType | str, open_enum_validator(TokenRequestedType)]
