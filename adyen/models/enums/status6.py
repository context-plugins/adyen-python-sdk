from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status6(str, Enum):
    """The status you want to change to, The status of the sweep. If not provided, by default, this is set to
    **active**.

    Possible values:

     * **active**: the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.

     * **inactive**: the sweep is disabled and cannot be triggered., The status of the transaction rule. If you provide
            a ``startDate`` in the request, the rule is automatically created
    with an **active** status.

    Possible values: **active**, **inactive**., The status of the webhook setting. Possible values:

    * **active**: You receive a balance webhook if any of the conditions in this setting are met.
    * **inactive**: You do not receive a balance webhook even if the conditions in this settings are met., The status of
        the recurring top-up. If not provided, by default, this is set to **active**.

    Possible values:

     * **active**: the top up is enabled and funds will be pulled in.

     * **inactive**: the top up is disabled and cannot be triggered."""

    ACTIVE = "active"
    INACTIVE = "inactive"

    __str__ = str.__str__


Status6OrStr: TypeAlias = Annotated[Status6 | str, open_enum_validator(Status6)]
