from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type33(str, Enum):
    """Type of entity.

    Possible values: **LegalEntity**, **BankAccount**, **Document**."""

    BANK_ACCOUNT = "BankAccount"
    DOCUMENT = "Document"
    LEGAL_ENTITY = "LegalEntity"

    __str__ = str.__str__


Type33OrStr: TypeAlias = Annotated[Type33 | str, open_enum_validator(Type33)]
