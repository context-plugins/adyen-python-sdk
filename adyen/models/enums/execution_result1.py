from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExecutionResult1(str, Enum):
    """The status of the payout execution.

    Possible values:
    - **succeeded**: The payout was sent successfully.
    - **failed**: The payout could not be sent because an error occurred.
    - **skipped**: The payout was not triggered as expected."""

    FAILED = "failed"
    SUCCEEDED = "succeeded"
    SKIPPED = "skipped"

    __str__ = str.__str__


ExecutionResult1OrStr: TypeAlias = Annotated[ExecutionResult1 | str, open_enum_validator(ExecutionResult1)]
