from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status21(str, Enum):
    """The status of the reassignment. Possible values:
     * ``reassignmentInProgress``: the terminal was boarded and is now scheduled to remove the configuration. Wait for
            the terminal to synchronize with the Adyen platform.
     * ``deployed``: the terminal is deployed and reassigned.
     * ``inventory``: the terminal is in inventory and cannot process transactions.
     * ``boarded``: the terminal is boarded to a store, or a merchant account representing a store, and can process
            transactions."""

    BOARDED = "boarded"
    DEPLOYED = "deployed"
    INVENTORY = "inventory"
    REASSIGNMENT_IN_PROGRESS = "reassignmentInProgress"

    __str__ = str.__str__


Status21OrStr: TypeAlias = Annotated[Status21 | str, open_enum_validator(Status21)]
