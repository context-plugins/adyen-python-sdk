from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TokenizationStoreOperationType(str, Enum):
    """The operation performed on the token. Possible values:

    * **created**: the token has been created.
    * **updated**: the existing token has been updated.
    * **alreadyExisting**: the details have already been stored."""

    CREATED = "created"
    UPDATED = "updated"
    ALREADY_EXISTING = "alreadyExisting"

    __str__ = str.__str__


TokenizationStoreOperationTypeOrStr: TypeAlias = Annotated[
    TokenizationStoreOperationType | str, open_enum_validator(TokenizationStoreOperationType)
]
