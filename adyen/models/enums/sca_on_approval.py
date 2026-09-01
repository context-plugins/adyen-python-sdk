from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaOnApproval(str, Enum):
    """Shows the status of the Strong Customer Authentication (SCA) process.

    Possible values: **required**, **notApplicable**."""

    COMPLETED = "completed"
    NOT_APPLICABLE = "notApplicable"
    REQUIRED = "required"

    __str__ = str.__str__


ScaOnApprovalOrStr: TypeAlias = Annotated[ScaOnApproval | str, open_enum_validator(ScaOnApproval)]
