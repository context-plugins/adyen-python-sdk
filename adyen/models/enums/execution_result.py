from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExecutionResult(str, Enum):
    FAILED = "failed"
    SUCCEEDED = "succeeded"
    SKIPPED = "skipped"

    __str__ = str.__str__


ExecutionResultOrStr: TypeAlias = Annotated[ExecutionResult | str, open_enum_validator(ExecutionResult)]
