from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContractType(str, Enum):
    """The contract type of the grant offer. Possible value: **cashAdvance**, **loan**., The contract type of the offer.

    Possible values:
    * **loan**
    * **cashAdvance**"""

    CASH_ADVANCE = "cashAdvance"
    LOAN = "loan"

    __str__ = str.__str__


ContractTypeOrStr: TypeAlias = Annotated[ContractType | str, open_enum_validator(ContractType)]
