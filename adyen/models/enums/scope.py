from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Scope(str, Enum):
    """The scope to which the transfer limit applies. Possible values:
    * **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.
    * **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in
        a day."""

    PER_DAY = "perDay"
    PER_TRANSACTION = "perTransaction"

    __str__ = str.__str__


ScopeOrStr: TypeAlias = Annotated[Scope | str, open_enum_validator(Scope)]
