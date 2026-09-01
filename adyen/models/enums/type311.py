from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type311(str, Enum):
    BANK_ACCOUNT = "BankAccount"
    DOCUMENT = "Document"
    LEGAL_ENTITY = "LegalEntity"
    PRODUCT = "product"

    __str__ = str.__str__


Type311OrStr: TypeAlias = Annotated[Type311 | str, open_enum_validator(Type311)]
