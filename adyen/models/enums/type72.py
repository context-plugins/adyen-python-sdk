from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type72(str, Enum):
    """The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by
    default, this is set to **push**.

    Possible values:

     * **push**: _push out funds_ to a destination balance account or transfer instrument.

     * **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account."""

    PULL = "pull"
    PUSH = "push"

    __str__ = str.__str__


Type72OrStr: TypeAlias = Annotated[Type72 | str, open_enum_validator(Type72)]
