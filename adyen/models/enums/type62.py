from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type62(str, Enum):
    """The schedule type.

    Possible values:

    * **cron**: push out funds based on a ``cronExpression``.

    * **daily**: push out funds daily at 07:00 AM CET.

    * **weekly**: push out funds every Monday at 07:00 AM CET.

    * **monthly**: push out funds every first of the month at 07:00 AM CET.

    * **balance**: execute the sweep instantly if the ``triggerAmount`` is reached."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    BALANCE = "balance"
    CRON = "cron"

    __str__ = str.__str__


Type62OrStr: TypeAlias = Annotated[Type62 | str, open_enum_validator(Type62)]
